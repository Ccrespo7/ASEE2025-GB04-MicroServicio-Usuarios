from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.usuario_schema import UserCreate, UserResponse
from app.services.auth_service import register_user,get_user_by_email
from app.core.database import get_db

router = APIRouter()

@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register(data: UserCreate, db: Session = Depends(get_db)):
    try:
        user = register_user(data, db)
        return user
    except ValueError as e:
        raise HTTPException(status_code=409, detail=str(e))

@router.get("/{email}", response_model=UserResponse, status_code=status.HTTP_200_OK)
def get_user(email: str, db: Session = Depends(get_db)):
    user = get_user_by_email(email, db)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user
