import sqlite3
from sqlmodel import Field, SQLModel,  Relationship



class Member(SQLModel, table=True):
    id: int | None = Field(index=True, default=None, primary_key=True)
    name: str #= Field(index=True)
    email: str
    carte_access_id: str | None = Field(default=None, foreign_key="access_card.id")

    registrations: list["Registration"] = Relationship(back_populates="member", cascade_delete=True)
    access_card : "Access_card" = Relationship(back_populates="member")

class Access_card(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    unique_number: str | None = Field(default=None)

    member : Member = Relationship(back_populates="access_card")

class Registration(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    member_id: int | None = Field(default=None, foreign_key="member.id", ondelete="CASCADE")
    course_id: int | None = Field(default=None, foreign_key="course.id", ondelete="CASCADE")
    registration_date: str

    member : Member = Relationship(back_populates="registrations")
    course : "Course" = Relationship(back_populates="registrations")


class Course(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    sport_type: str
    hour: str
    max_capacity: int   
    coach_id: int| None = Field(default=None, foreign_key="coach.id")
    max_capacity: str    
    coach_id: int| None = Field(default=None, foreign_key="coach.id", ondelete="CASCADE")

    registrations : list[Registration] = Relationship(back_populates="course", cascade_delete=True)
    coach : "Coach" = Relationship(back_populates="courses_list")

class Coach(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    sport_speciality: str

    courses_list : list[Course] = Relationship(back_populates="coach", cascade_delete=True) 