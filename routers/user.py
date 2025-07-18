from fastapi import APIRouter, Depends
from schemas import users
from sqlalchemy.orm import Session
from database import get_db
import models
from repository import user

router = APIRouter(tags=["Users"], prefix="/user")


@router.post("/create")
def create(request: users.CreateUser, db: Session = Depends(get_db)):
    return user.create(request, db)


@router.get("/show")
def show_all(db: Session = Depends(get_db)):
    return db.query(models.Users).all()


@router.get("/show_by_id/{user_id}")
def show(user_id: int, db: Session = Depends(get_db)):
    return user.show_by_id(user_id, db)


@router.put("/update/{user_id}")
def update(user_id: int, request: users.UpdateUser, db: Session = Depends(get_db)):
    return user.update(user_id, request, db)


@router.delete("/delete/{user_id}")
def delete(user_id: int, db: Session = Depends(get_db)):
    return user.delete(user_id, db)
