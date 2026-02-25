from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import engine, Base, SessionLocal
import models
import schemas
import crud

Base.metadata.create_all(bind=engine)

app = FastAPI(title="ЧЛМТ")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/groups/", response_model=schemas.Group)
def create_group(group: schemas.GroupCreate, db: Session = Depends(get_db)):
    return crud.create(db, models.Group(**group.dict()))

@app.get("/groups/", response_model=list[schemas.Group])
def get_groups(db: Session = Depends(get_db)):
    return crud.get_all(db, models.Group)

@app.delete("/groups/{group_id}")
def delete_group(group_id: int, db: Session = Depends(get_db)):
    crud.delete(db, models.Group, group_id)
    return {"message": "Deleted"}

@app.post("/students/", response_model=schemas.Student)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    return crud.create(db, models.Student(**student.dict()))

@app.get("/students/", response_model=list[schemas.Student])
def get_students(db: Session = Depends(get_db)):
    return crud.get_all(db, models.Student)

@app.delete("/students/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    crud.delete(db, models.Student, student_id)
    return {"message": "Deleted"}

@app.post("/teachers/", response_model=schemas.Teacher)
def create_teacher(teacher: schemas.TeacherCreate, db: Session = Depends(get_db)):
    return crud.create(db, models.Teacher(**teacher.dict()))


@app.get("/teachers/", response_model=list[schemas.Teacher])
def get_teachers(db: Session = Depends(get_db)):
    return crud.get_all(db, models.Teacher)

@app.post("/subjects/", response_model=schemas.Subject)
def create_subject(subject: schemas.SubjectCreate, db: Session = Depends(get_db)):
    return crud.create(db, models.Subject(**subject.dict()))

@app.get("/subjects/", response_model=list[schemas.Subject])
def get_subjects(db: Session = Depends(get_db)):
    return crud.get_all(db, models.Subject)

@app.post("/classrooms/", response_model=schemas.Classroom)
def create_classroom(classroom: schemas.ClassroomCreate, db: Session = Depends(get_db)):
    return crud.create(db, models.Classroom(**classroom.dict()))

@app.get("/classrooms/", response_model=list[schemas.Classroom])
def get_classrooms(db: Session = Depends(get_db)):
    return crud.get_all(db, models.Classroom)

@app.post("/schedule/", response_model=schemas.Schedule)
def create_schedule(schedule: schemas.ScheduleCreate, db: Session = Depends(get_db)):
    return crud.create_schedule(db, schedule)

@app.get("/schedule/", response_model=list[schemas.Schedule])
def get_schedule(db: Session = Depends(get_db)):
    return crud.get_all(db, models.Schedule)