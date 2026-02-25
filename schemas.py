from pydantic import BaseModel

class BaseConfig(BaseModel):
    class Config:
        from_attributes = True

class GroupCreate(BaseModel):
    name: str

class Group(BaseConfig):
    id: int
    name: str

class StudentCreate(BaseModel):
    full_name: str
    group_id: int

class Student(BaseConfig):
    id: int
    full_name: str
    group_id: int

class TeacherCreate(BaseModel):
    full_name: str

class Teacher(BaseConfig):
    id: int
    full_name: str

class SubjectCreate(BaseModel):
    name: str

class Subject(BaseConfig):
    id: int
    name: str

class ClassroomCreate(BaseModel):
    name: str

class Classroom(BaseConfig):
    id: int
    name: str

class ScheduleCreate(BaseModel):
    group_id: int
    teacher_id: int
    subject_id: int
    classroom_id: int
    day_of_week: int
    lesson_number: int

class Schedule(BaseConfig):
    id: int
    group_id: int
    teacher_id: int
    subject_id: int
    classroom_id: int
    day_of_week: int
    lesson_number: int