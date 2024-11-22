from models import *
from faker import Faker
from init_db import *
from sqlmodel import Session, select
import random
from datetime import datetime, timedelta

fake = Faker()

sports_list = ["Yoga", "Pilate", "Crossfit", "Pump", "Musculation", "Bodycombat", "Boxe"]

def create_fake_members(num_members):
    with Session(engine) as session:
        fake_list = random.sample(range(10000, 100000), num_members)
        for i in range(num_members):
            access_card = Access_card(unique_number=fake_list[i])
            session.add(access_card)

            member = Member(
                name=fake.name(),
                email=fake.email(),
                access_card=access_card
            )
            session.add(member)
        session.commit()

# def create_fake_access_card(x):
#     session = Session(engine)
#     fake_list = random.sample(range(10000,100000),x)
#     for i in range(x):
#         access_card = Access_card(unique_number=fake_list[i])
#         session.add(access_card)
#     session.commit()
#     session.refresh(access_card)
#     session.close()


def create_fake_coaches(num_coaches):
    with Session(engine) as session:
        for i in range(num_coaches):
            sport_speciality = sports_list[i % len(sports_list)]
            coach = Coach(
                name=fake.name(),
                sport_speciality=sport_speciality
            )
            session.add(coach)
        session.commit()


def create_fake_courses(num_courses, start_time=9, end_time=17):
    with Session(engine) as session:
        day_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        hour_list = [f"{day} {h:02d}:00" for day in day_list for h in range(start_time, end_time)]

        for _ in range(num_courses):
            if not hour_list:
                print("No more available time slots.")
                break

            sport_course = random.choice(sports_list)
            chosen_hour = random.choice(hour_list)
            hour_list.remove(chosen_hour)

            coach = session.exec(select(Coach).where(Coach.sport_speciality == sport_course)).first()
            if not coach:
                print(f"No coach found for {sport_course}.")
                continue

            course = Course(
                sport_type=sport_course,
                hour=chosen_hour,
                max_capacity=10,
                coach_id=coach.id
            )
            session.add(course)
        session.commit()


def create_fake_registrations(num_registrations):
    with Session(engine) as session:
        course_ids = [course.id for course in session.exec(select(Course))]
        member_ids = [member.id for member in session.exec(select(Member))]

        registrations_done = 0

        for _ in range(num_registrations):
            if not course_ids or not member_ids:
                print("No courses or members available.")
                break

            chosen_course_id = random.choice(course_ids)
            chosen_member_id = random.choice(member_ids)

            course_registrations = session.exec(
                select(Registration).where(Registration.course_id == chosen_course_id)
            ).all()

            if len(course_registrations) < 10:
                registration = Registration(
                    member_id=chosen_member_id,
                    course_id=chosen_course_id,
                    registration_date=fake.date_time_between(start_date="-1y", end_date="now")
                )
                session.add(registration)
                registrations_done += 1
            else:
                print(f"Course {chosen_course_id} is already full.")

        session.commit()




def create_disponibility_list():
    day_list = ["Monday", "Tuedsay", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    hour_list=[]
    for day in day_list:
        for h in range(9,17):
            hour_list.append([day, str(h)]) 
    session = Session(engine)
    statement = select(Course.hour)
    result_heure_cours = session.exec(statement)
    heure_cours_list = []
    for heure in result_heure_cours:
        if heure[-2].isdigit():
            hour_temp_list = [heure[:-3], heure[-3:]]
            heure_cours_list.append(hour_temp_list)
        else:
            hour_temp_list = [heure[:-2], heure[-2:]]
            heure_cours_list.append(hour_temp_list)
    list_dispo = []
    for h in hour_list:
        if h not in heure_cours_list:
            list_dispo.append(h)
    return(list_dispo)

    
# class Registration(SQLModel, table=True):
#     id: int | None = Field(default=None, primary_key=True)
#     member_id: str | None = Field(default=None, foreign_key="member.id")
#     course_id: str | None = Field(default=None, foreign_key="course.id")
#     registration_date: str

#     member : Member = Relationship(back_populates="registrations")
#     course : "Course" = Relationship(back_populates="registrations")