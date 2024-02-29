# backend/app/crud/crud_estudio.py

from sqlalchemy.orm import Session
from ..models.models import Base_Estudio
from ..models.schemas import BaseEstudioCreate  # Asegúrate de que este sea el nombre correcto del esquema Pydantic

def get_estudio(db: Session, estudio_id: int):
    return db.query(Base_Estudio).filter(Base_Estudio.id == estudio_id).first()

def get_estudios(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Base_Estudio).offset(skip).limit(limit).all()

def create_estudio(db: Session, estudio: BaseEstudioCreate):
    db_estudio = Base_Estudio(**estudio.dict())
    db.add(db_estudio)
    db.commit()
    db.refresh(db_estudio)
    return db_estudio

# Aquí agregarías funciones para actualizar y eliminar
