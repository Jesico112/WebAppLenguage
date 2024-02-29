# backend/app/dependencies.py

# Si database.py está en la misma carpeta que dependencies.py
from db.database import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
