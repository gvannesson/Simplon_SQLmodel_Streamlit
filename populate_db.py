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
        for x in range(9,17):
            hour_list.append([day, x]) 
 
    for i in range(x):
        sport_course = random.choice(sports_list)
        print(sport_course)
        print(session.exec(select(Coach).where(Coach.sport_speciality==sport_course)).first().id)
        course = Course(sport_type=sport_course, hour="".join(random.choice(hour_list)), max_capacity=10, coach_id=session.exec(select(Coach).where(Coach.sport_speciality==sport_course)).first().id)
        session.add(course)
    session.commit()
    session.refresh(course)
    session.close()
    
