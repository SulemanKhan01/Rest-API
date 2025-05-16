from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import schemas, models, crud
from database import get_db

router = APIRouter()

@router.post("/users/", response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)

@router.get("/users/", response_model=list[schemas.UserOut])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_users(db, skip, limit)

@router.get("/users/{user_id}", response_model=schemas.UserOut)
def read_user(user_id: int, db: Session = Depends(get_db)):
    return crud.get_user(db, user_id)

@router.put("/users/{user_id}", response_model=schemas.UserOut)
def update_user(user_id: int, user_data: schemas.UserUpdate, db: Session = Depends(get_db)):
    return crud.update_user(db, user_id, user_data)

@router.delete("/users/{user_id}", response_model=schemas.UserOut)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    return crud.delete_user(db, user_id)
