import streamlit as st
from models import *
from faker import Faker
from init_db import *
import pandas as pd
import random
import datetime

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


day_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
hour_list = [f"{day} {h:02d}:00" for day in day_list for h in range(9, 17)]
session = Session(engine)
statement = select(Course.hour)
result_course_hour = session.exec(statement)
course_list_hour = []
for hour in result_course_hour:
    course_list_hour.append(hour)
list_dispo = []
for h in hour_list:
    if h not in course_list_hour:
        list_dispo.append(h)


sports_list = ["Yoga", "Pilate", "Crossfit", "Pump","Musculation", "Bodycombat", "Boxe"]

st.markdown("<div class='main-header'>Management of the gym - ADMIN Part🎉</div>", unsafe_allow_html=True)
st.sidebar.title("Management of the gym - ADMIN Part🎉")

if 'reset' not in st.session_state:
    st.session_state.reset = False

if st.session_state.reset:
    st.session_state.coaching_management = False
    st.session_state.validate_new_coach = False
    st.session_state.validate_coach_choice_modification = False
    st.session_state.validate_coach_deleting_modification = False
    st.session_state.validate_new_sport_course = False
    st.session_state.course_management=False
    st.session_state.validate_course_to_modify = False
    st.session_state.validate_sport_course_to_delete = False
    st.session_state.reset = False

if "validate_sport_course_to_delete" not in st.session_state:
    st.session_state.validate_sport_course_to_delete = False

if "validate_course_to_modify" not in st.session_state:
    st.session_state.validate_course_to_modify = False

if "validate_new_sport_course" not in st.session_state:
    st.session_state.validate_new_sport_course = False

if "validate_coach_choice_modification" not in st.session_state:
    st.session_state.validate_coach_choice_modification = False

if "validate_coach_deleting_modification" not in st.session_state:
    st.session_state.validate_coach_deleting_modification = False

if "coaching_management" not in st.session_state:
    st.session_state.coaching_management = False

if "validate_new_coach" not in st.session_state:
    st.session_state.validate_new_coach = False    

if "course_management" not in st.session_state:
    st.session_state.course_management = False

if not st.session_state.coaching_management:
    if st.sidebar.button("Coaching management"):
        st.session_state.coaching_management=True
        st.session_state.course_management = False
        st.rerun()


if st.session_state.coaching_management:
    coaching_management_radio = st.radio("Coaching management",["Add a coach", "Modify a coach", "Delete a coach"])
    if coaching_management_radio == "Add a coach":
        st.text_input('Name of our new coach',key="new_coach_name")
        st.selectbox("Sport of our new coach", options=sports_list, key="new_coach_sport")
        if not st.session_state.validate_new_coach:
            if st.button("Validate"):
                st.session_state.validate_new_coach = True
                st.rerun()
        if st.session_state.validate_new_coach:
            session = Session(engine)
            coach = Coach(name=st.session_state.new_coach_name, sport_speciality=st.session_state.new_coach_sport)
            session.add(coach)
            session.commit()
            session.refresh(coach)
            session.close()
            st.session_state.reset = True
            st.rerun()
    if coaching_management_radio == "Modify a coach":
        session=Session(engine)
        coach_list = session.exec(select(Coach))
        st.selectbox("Which coach do you want to modify", options=[coach.name for coach in coach_list], key="modifying_coach_selectbox")
        if not st.session_state.validate_coach_choice_modification:
            if st.button("Validate"):
                st.session_state.validate_coach_choice_modification = True
                st.rerun()
        if st.session_state.validate_coach_choice_modification:
            session = Session(engine)
            with st.form("Validate coach modification"):
                name_modification = st.text_input("Name modification", key="name_modification")
                sport_coach_modification = st.selectbox("Sport of our new coach", options=sports_list, key="sport_coach_modification")
                submitted = st.form_submit_button("Submit")
                if submitted:
                    statement = select(Coach).where(Coach.name == st.session_state.modifying_coach_selectbox)
                    results = session.exec(statement).first()
                    results.name = name_modification
                    results.sport_speciality = sport_coach_modification
                    session.add(results)
                    session.commit()
                    session.refresh(results)
                    session.close()
                    st.session_state.reset = True
                    st.rerun()
    if coaching_management_radio == "Delete a coach":
        session=Session(engine)
        coach_list = session.exec(select(Coach))
        st.selectbox("Which coach do you want to delete", options=[coach.name for coach in coach_list], key="deleting_coach_selectbox")
        if not st.session_state.validate_coach_deleting_modification:
            if st.button("Validate"):
                st.session_state.validate_coach_deleting_modification = True
                st.rerun()
        if st.session_state.validate_coach_deleting_modification:
            session = Session(engine)   
            with st.form("Validate coach deletion"):
                statement = select(Coach).where(Coach.name == st.session_state.deleting_coach_selectbox)
                results = session.exec(statement).all()
                for result in results:
                    session.delete(result)
                    session.commit()
                session.close()
                st.session_state.reset = True
                st.rerun()   
    


if not st.session_state.course_management:
    if st.sidebar.button("Course management"):
        st.session_state.course_management=True
        st.session_state.coaching_management = False
        st.rerun()

if st.session_state.course_management:
    course_management_radio = st.radio("Course management",["See course registration", "Add a course", "Modify a course", "Delete a course","Registration History"])
    if course_management_radio == "Add a course":
        st.selectbox("Sport of the new course", options=sports_list, key="new_course_sport")
        if not st.session_state.validate_new_sport_course:
            if st.button("Validate"):
                st.session_state.validate_new_sport_course = True
                st.rerun()
        if st.session_state.validate_new_sport_course:
            with st.form("Validate new course"):
                session = Session(engine)
                statement = select(Course)
                result_heure_cours = session.exec(statement)
                st.selectbox("Date of our new course", options=list_dispo, key="new_date_course")
                submitted = st.form_submit_button("Submit")
                if submitted:
                    new_course = Course(sport_type=st.session_state.new_course_sport, hour="".join(st.session_state.new_date_course), max_capacity=10, coach_id=session.exec(select(Coach).where(Coach.sport_speciality==st.session_state.new_course_sport)).first().id)
                    session.add(new_course)
                    session.commit()
                    session.refresh(new_course)
                    session.close()
                    st.session_state.reset = True
                    st.rerun()

    if course_management_radio == "Modify a course":
        session = Session(engine)
        statement = session.exec(select(Course))
        st.selectbox("Course to modify", options=[[course.sport_type, course.hour] for course in statement], key="course_to_modify")
        if not st.session_state.validate_course_to_modify:
            if st.button("Validate"):
                st.session_state.validate_course_to_modify = True
                st.rerun()
        if st.session_state.validate_course_to_modify:
            session = Session(engine)
            with st.form("Validate course modification"):
                list_dispo_course=list_dispo.copy()
                list_dispo_course.append(session.exec(select(Course.hour).where(Course.sport_type == st.session_state.course_to_modify[0]).where(Course.hour == st.session_state.course_to_modify[1])).first())
                sport_course_modification = st.selectbox("Sport of the course", options=sports_list, key="sport_course_modification")
                hour_course_modification = st.selectbox("New hour of the course", options=list_dispo_course, key="hour_course_modification")
                coach_course_modification = st.selectbox("New coach for the course", options = [coach.name for coach in session.exec(select(Coach))], key = "coach_course_modification")
                submitted = st.form_submit_button("Submit")
                if submitted:
                    statement = select(Course).where(Course.sport_type == st.session_state.course_to_modify[0]).where(Course.hour == st.session_state.course_to_modify[1])
                    results = session.exec(statement).first()
                    results.sport_type = sport_course_modification
                    results.hour = "".join(hour_course_modification)
                    results.coach_id = session.exec(select(Coach).where(Coach.name == coach_course_modification)).first().id
                    session.add(results)
                    session.commit()
                    session.refresh(results)
                    session.close()
                    st.session_state.reset = True
                    st.rerun()

    if course_management_radio == "Delete a course":
        st.selectbox("Sport of the course to delete", options=sports_list, key="course_to_delete_sport")
        if not st.session_state.validate_sport_course_to_delete:
            if st.button("Validate"):
                st.session_state.validate_sport_course_to_delete = True
                st.rerun()
        if st.session_state.validate_sport_course_to_delete:
            with st.form("Validate course to delete"):
                session = Session(engine)
                statement = select(Course).where(Course.sport_type == st.session_state.course_to_delete_sport)
                result = session.exec(statement).all()
                st.selectbox("Date of the course to delete", options=[heure.hour for heure in result], key="course_to_delete_hour")
                submitted = st.form_submit_button("Submit")
                if submitted:
                    statement= select(Course).where(Course.sport_type == st.session_state.course_to_delete_sport).where(Course.hour == st.session_state.course_to_delete_hour)
                    result = session.exec(statement).first()
                    session.delete(result)
                    session.commit()
                    session.close()
                    st.session_state.reset = True
                    st.rerun()


    if course_management_radio == "Registration History":
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
                st.write(pd.DataFrame(result_list), key="registration_history")

        registration_id = st.text_input("Enter the Registration ID to cancel:")
        if st.button("Cancel"):
            if registration_id.isdigit():
                registration_to_delete = session.get(Registration, int(registration_id))
                if registration_to_delete and registration_to_delete.member_id == selected_member_id:
                    session.delete(registration_to_delete)
                    session.commit()
                    st.rerun()
                    st.success(f"Registration with ID {registration_id} has been canceled.")
                else:
                    st.error("Registration not found or does not belong to the selected member.")
            else:
                st.warning("Please enter a valid numeric Registration ID.")

            session.close()

                   # if not st.session_state.validate_new_sport_course:
        #     if st.button("Validate"):
        #         st.session_state.validate_new_sport_course = True
        #         st.rerun()
        # if st.session_state.validate_new_sport_course:
        #     with st.form("Validate new course"):
        #         session = Session(engine)
        #         statement = select(Course)
        #         result_heure_cours = session.exec(statement)
        #         st.selectbox("Date of our new course", options=list_dispo, key="new_date_course")
        #         submitted = st.form_submit_button("Submit")
        #         if submitted:
        #             new_course = Course(sport_type=st.session_state.new_course_sport, hour="".join(st.session_state.new_date_course), max_capacity=10, coach_id=1)
        #             session.add(new_course)
        #             session.commit()
        #             session.refresh(new_course)
        #             session.close()
        #             st.session_state.reset = True
        #             st.rerun()