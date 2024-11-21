from models import *
from faker import Faker
from init_db import *
import random
import datetime


fake=Faker()

sports_list = ["yoga", "pilate", "crossfit", "pump","musculation", "bodycombat", "boxe"]

def create_fake_members(x):
    session = Session(engine)
    fake_list = random.sample(range(10000,100000),x)
    for i in range(x):
        access_card = Access_card(unique_number=fake_list[i])
        session.add(access_card)
        member = Member(name=fake.name(), email=fake.email(), access_card=access_card)
        session.add(member)
        session.commit()
        session.refresh(member)
    session.close()


# def create_fake_access_card(x):
#     session = Session(engine)
#     fake_list = random.sample(range(10000,100000),x)
#     for i in range(x):
#         access_card = Access_card(unique_number=fake_list[i])
#         session.add(access_card)
#     session.commit()
#     session.refresh(access_card)
#     session.close()


def create_fake_coaches(x):
    session = Session(engine)
    for i in range(x):
        coach = Coach(name=fake.name(), sport_speciality=sports_list[i])
        session.add(coach)
        session.commit()
    session.refresh(coach)
    session.close()



def create_fake_course(x):
    session = Session(engine)
    day_list = ["Monday", "Tuedsay", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    hour_list=[]
    for day in day_list:
        for h in range(9,17):
            hour_list.append([day, str(h)]) 
 
    for _ in range(x):
        sport_course = random.choice(sports_list)
        chosen_hour = random.choice(hour_list)
        hour_index = hour_list.index(chosen_hour)
        hour_list.pop(hour_index)
        print(sport_course)
        print(random.choice(hour_list))
        course = Course(sport_type=sport_course, hour="".join(chosen_hour), max_capacity=10, coach_id=session.exec(select(Coach).where(Coach.sport_speciality==sport_course)).first().id)
        session.add(course)
    session.commit()
    session.refresh(course)
    session.close()


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