from sqlalchemy.orm import Session
from app.models.usuario_model import User
from app.schemas.usuario_schema import UserCreate, UserResponse
from fastapi import HTTPException, status
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str):
    return pwd_context.hash(password)

def register_user(data: UserCreate, db: Session):
    # Comprobar si el usuario ya existe
    existing_user = db.query(User).filter(User.email == data.email).first()
    if existing_user:
        raise HTTPException(status_code=409, detail="El usuario ya existe")

    # Crear el usuario nuevo
    #hashed_pw = get_password_hash(data.password)
    new_user = User(
        email=data.email,
        password=data.password,
        display_name=data.display_name
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user_by_email(email: str, db: Session):
    user = db.query(User).filter(User.email == email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")
    return user