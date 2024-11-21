import sqlite3
from sqlmodel import Field, Session, SQLModel, create_engine, select, or_, Relationship
from typing import Optional


class Member(SQLModel, table=True):
    id: int | None = Field(index=True, default=None, primary_key=True)
    name: str #= Field(index=True)
    email: str
    carte_access_id: str | None = Field(default=None, foreign_key="access_card.id")

    registrations: list["Registration"] = Relationship(back_populates="member")
    access_card : "Access_card" = Relationship(back_populates="member")

class Access_card(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    unique_number: str | None = Field(default=None)

    member : Member = Relationship(back_populates="access_card")

class Registration(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    member_id: int | None = Field(default=None, foreign_key="member.id")
    course_id: int | None = Field(default=None, foreign_key="course.id")
    registration_date: str

    member : Member = Relationship(back_populates="registrations")
    course : "Course" = Relationship(back_populates="registrations")


class Course(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    sport_type: str
    hour: str
    max_capacity: int   
    coach_id: int| None = Field(default=None, foreign_key="coach.id")

    registrations : list[Registration] = Relationship(back_populates="course")
    coach : "Coach" = Relationship(back_populates="courses_list")

class Coach(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    sport_speciality: str

    courses_list : Optional[Course] = Relationship(back_populates="coach")
