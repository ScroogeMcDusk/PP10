from sqlalchemy.orm import Session
from fastapi import HTTPException
import models

def create(db: Session, obj):
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


def get_all(db: Session, model):
    return db.query(model).all()


def delete(db: Session, model, obj_id: int):
    obj = db.query(model).get(obj_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Not found")
    db.delete(obj)
    db.commit()

def check_schedule_conflicts(db: Session, schedule):
    conflict = db.query(models.Schedule).filter(
        models.Schedule.day_of_week == schedule.day_of_week,
        models.Schedule.lesson_number == schedule.lesson_number,
        (
            (models.Schedule.teacher_id == schedule.teacher_id) |
            (models.Schedule.classroom_id == schedule.classroom_id) |
            (models.Schedule.group_id == schedule.group_id)
        )
    ).first()

    if conflict:
        raise HTTPException(
            status_code=400,
            detail="Schedule conflict detected"
        )

def create_schedule(db: Session, schedule_data):
    check_schedule_conflicts(db, schedule_data)
    schedule = models.Schedule(**schedule_data.dict())
    return create(db, schedule)