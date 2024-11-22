import streamlit as st
from models import *
from init_db import *
from populate_db import *
import pandas as pd
from datetime import datetime
from sqlmodel import select, Session

# Custom CSS for styling
st.markdown(
    """
    <style>
        /* Center the header and apply styling */
        .main-header {
            text-align: center;
            font-size: 2.5em;
            color: #556B2F; /* Olive green */
            font-weight: bold;
            margin-bottom: 30px;
            font-family: Arial, sans-serif;
        }

        /* Sidebar styling */
        .sidebar .sidebar-content {
            background-color: #f8f9f5; /* Light eucalyptus background */
            padding: 20px;
            border-right: 2px solid #d2d7c7; /* Soft olive border */
        }

        /* Dropdown styling */
        .stSelectbox [data-baseweb="select"] {
            border: 1px solid #556B2F; /* Olive green border */
            border-radius: 5px;
        }

        /* General font styling for body */
        body {
            font-family: 'Arial', sans-serif;
            color: #333333;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Header
st.markdown("<div class='main-header'>Gym Member Portal</div>", unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.selectbox(
    "Choose a Page:",
    ["Register in a Class", "Registration History"],
)

session = Session(engine)

if page == "Register in a Class":
    st.header("Register in a Class")
    st.write("Check out the available classes below:")

    sports = session.exec(select(Course.sport_type).distinct()).all()
    sports_list = [sport for sport in sports]

    if not sports_list:
        st.warning("No sports available at the moment.")
    else:
        members = session.exec(select(Member)).all()
        member_list = {member.name: member.id for member in members}
        selected_member_name = st.selectbox("Select Member", options=member_list.keys())
        selected_member_id = member_list[selected_member_name]

        selected_sport = st.selectbox("Available courses", options=sports_list, key="course_available_for_registration")
        statement = select(Course).where(Course.sport_type == selected_sport)
        result = session.exec(statement).all()

        if not result:
            st.warning("No classes available for this sport.")
        else:
            preferred_time = st.selectbox(
                "Choose your preferred time",
                options=[course.hour for course in result],
                key="preferred_time",
            )

            if st.button("Validate"):
                statement_course = statement.where(Course.hour == preferred_time)
                result_course = session.exec(statement_course).first()

                if result_course:
                    new_registration = Registration(
                        member_id=selected_member_id,
                        course_id=result_course.id,
                        registration_date=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    )
                    course_registrations = session.exec(select(Registration).where(Registration.course_id == result_course.id)).all()
                    print(f"####{course_registrations}")
                    if len(course_registrations) < 10 and selected_member_id not in [registration.member_id for registration in course_registrations]:
                        session.add(new_registration)
                        session.commit()
                        st.success(f"Success! {selected_member_name} has registered for the course.")
                    else:
                        if len(course_registrations) >= 10:
                            st.error("The selected course is full!")
                        if selected_member_id in [registration.member_id for registration in course_registrations]:
                            st.error("déjà inscrit")
                else:
                    st.error("The selected course is no longer available.")

elif page == "Registration History":
    st.header("Registration History")
    st.write("Filter registrations by member and manage them below.")

    # Retrieve all members
    members = session.exec(select(Member)).all()
    member_list = {member.name: member.id for member in members}

    if not member_list:
        st.info("No members available.")
    else:
        # Select a member from the list
        selected_member_name = st.selectbox("Select Member", options=member_list.keys())
        selected_member_id = member_list[selected_member_name]

        # Retrieve registrations for the selected member
        statement = select(Registration).join(Course).where(Registration.member_id == selected_member_id)
        result = session.exec(statement).all()

        if not result:
            st.info(f"No registrations found for {selected_member_name}.")
        else:
            # Display registrations for the selected member
            result_list = [
                {
                    "ID": reg.id,
                    "Sport": reg.course.sport_type,
                    "Hour": reg.course.hour
                }
                for reg in result
            ]
            st.write(pd.DataFrame(result_list))

            # Cancel registration functionality
            registration_id = st.text_input("Enter the Registration ID to cancel:")
            if st.button("Cancel"):
                if registration_id.isdigit():
                    registration_to_delete = session.get(Registration, int(registration_id))
                    if registration_to_delete and registration_to_delete.member_id == selected_member_id:
                        session.delete(registration_to_delete)
                        session.commit()
                        st.success(f"Registration with ID {registration_id} has been canceled.")
                    else:
                        st.error("Registration not found or does not belong to the selected member.")
                else:
                    st.warning("Please enter a valid numeric Registration ID.")

session.close()
