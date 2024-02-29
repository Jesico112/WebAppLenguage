# initialize_db.py

from db.database import Base, engine
from models.models import Base_Estudio  # Asegúrate de importar todas tus clases de modelo aquí

def initialize_db():
    # Esto creará todas las tablas en la base de datos basadas en los modelos importados
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    initialize_db()


