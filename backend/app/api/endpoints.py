# backend/app/api/endpoints.py

from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from ..crud.crud import create_estudio, get_estudio, get_estudios  # Asegúrate de tener estas funciones definidas en crud_estudio.py
from ..models.schemas import BaseEstudioCreate, BaseEstudio
from .dependencies import get_db

router = APIRouter()

@router.post("/estudios/", response_model=BaseEstudio)
def create_estudio_endpoint(estudio: BaseEstudioCreate, db: Session = Depends(get_db)):
    return create_estudio(db=db, estudio=estudio)

@router.get("/estudios/", response_model=List[BaseEstudio])
def read_estudios(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    estudios = get_estudios(db, skip=skip, limit=limit)
    return estudios

@router.get("/estudios/{estudio_id}", response_model=BaseEstudio)
def read_estudio(estudio_id: int, db: Session = Depends(get_db)):
    db_estudio = get_estudio(db, estudio_id=estudio_id)
    if db_estudio is None:
        raise HTTPException(status_code=404, detail="Estudio not found")
    return db_estudio

# Aquí agregarías endpoints para actualizar y eliminar


