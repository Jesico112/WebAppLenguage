# backend/app/schemas.py

from pydantic import BaseModel
from typing import Optional
import datetime

# Esquema para la entrada de datos
class BaseEstudioCreate(BaseModel):
    Ingles: str
    Espanol: str
    Fonetica: Optional[str] = None
    Pronunciacion_simple: Optional[str] = None
    Nivel: str
    Categoria: str
    Tipo_de_repaso: str
    Date: Optional[datetime.datetime] = None

# Esquema para la salida de datos
class BaseEstudio(BaseModel):
    id: int
    Ingles: str
    Espanol: str
    Fonetica: Optional[str] = None
    Pronunciacion_simple: Optional[str] = None
    Nivel: str
    Categoria: str
    Tipo_de_repaso: str
    Date: datetime.datetime

    class Config:
        orm_mode = True
