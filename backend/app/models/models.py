# models/models.py

from sqlalchemy import Column, Integer, String, DateTime
from db.database import Base
from pydantic import BaseModel
import datetime

# Tu esquema BaseEstudio con Pydantic
class EstudioBase(BaseModel):
    Ingles: str
    Espanol: str
    Fonetica: str
    Pronunciacion_simple: str
    Nivel: str
    Categoria: str
    Tipo_de_repaso: str
    Date: datetime.datetime

# Tu modelo SQLAlchemy
class Base_Estudio(Base):
    __tablename__ = "ingles"

    id = Column(Integer, primary_key=True, index=True)
    Ingles = Column(String, index=True)
    Espanol = Column(String, index=True)
    Fonetica = Column(String, index=True)
    Pronunciacion_simple = Column(String, index=True)
    Nivel = Column(String, index=True)
    Categoria = Column(String, index=True)
    Tipo_de_repaso = Column(String, index=True)
    Date = Column(DateTime, default=datetime.datetime.utcnow)
