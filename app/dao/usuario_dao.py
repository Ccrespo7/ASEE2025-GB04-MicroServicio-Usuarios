from sqlalchemy.orm import Session
from app.models.usuario_model import User
from typing import Optional

def get_user_by_email(db: Session, email: str):
    """
    Retorna una instancia User o None.
    """
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, user: User):
    """
    Persiste una instancia User y la retorna con id/refresh.
    """
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def update_user(db: Session, email: str, **kwargs):
    """
    Actualiza los campos del usuario especificados en kwargs
    """
    db_user = db.query(User).filter(User.email == email).first()
    if not db_user:
        return None
    
    # Actualizar solo los campos proporcionados
    for key, value in kwargs.items():
        if value is not None and hasattr(db_user, key):
            setattr(db_user, key, value)
    
    db.commit()
    db.refresh(db_user)
    return db_user