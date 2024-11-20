import streamlit as st
from models import *
from faker import Faker
from init_db import *
import random
import datetime

sports_list = ["yoga", "pilate", "crossfit", "pump","musculation", "bodycombat", "boxe"]

st.markdown("Management of the gym - ADMIN Part🎉")
st.sidebar.markdown("Management of the gym - ADMIN Part🎉")

if 'reset' not in st.session_state:
    st.session_state.reset = False

if st.session_state.reset:
    st.session_state.coaching_management = False
    st.session_state.validate_new_coach = False
    st.session_state.validate_coach_choice_modification = False
    st.session_state.reset = False

if "validate_coach_choice_modification" not in st.session_state:
    st.session_state.validate_coach_choice_modification = False

if "coaching_management" not in st.session_state:
    st.session_state.coaching_management = False

if "validate_new_coach" not in st.session_state:
    st.session_state.validate_new_coach = False    

if "course_management" not in st.session_state:
    st.session_state.course_management = False

if not st.session_state.coaching_management:
    if st.sidebar.button("Coaching management"):
        st.session_state.coaching_management=True
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
                    print("good")
                    statement = select(Coach).where(Coach.name == st.session_state.modifying_coach_selectbox)
                    results = session.exec(statement).first()
                    print("good1")
                    # results.name = st.session_state.name_modification
                    results.name = name_modification
                    print("good2")
                    results.sport_speciality = sport_coach_modification
                    print("good3")
                    print(results)
                    print(results.name)
                    session.add(results)
                    print("good4")
                    session.commit()
                    session.refresh(results)
                    session.close()
                    st.session_state.reset = True
                    st.rerun()


if not st.session_state.course_management:
    if st.sidebar.button("Course management"):
        st.session_state.course_management=True
        st.rerun()

if st.session_state.course_management:
    course_management_radio = st.radio("Course management",["See course registration", "Add a course", "modify a course", "Delete a course", "Cancel a registration"])