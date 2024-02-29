from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
#from models.models import Base_Estudio  # Asegúrate de importar tus modelos aquí

# Configuración de la base de datos
SQLALCHEMY_DATABASE_URL = "sqlite:///test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Crea una instancia de Base que se utilizará para definir los modelos
Base = declarative_base()

def initialize_db():
    # Crea todas las tablas en la base de datos
    Base.metadata.create_all(engine)

# Ejecuta la función de inicialización si este script se ejecuta como script principal
if __name__ == "__main__":
    initialize_db()
