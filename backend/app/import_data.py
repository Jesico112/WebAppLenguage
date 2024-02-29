import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.models import Base_Estudio  # Actualiza esta ruta si es necesario

# Especifica el nombre de tu archivo Excel y la ruta al archivo de base de datos
excel_file = r'C:\Curso Python\my_aplication_web\DataBase.xlsx'  # Usa 'r' para una ruta raw
sqlite_db_path = 'sqlite:///./test.db'  # Asegúrate de que esta ruta sea correcta

# Crea una instancia del motor y de la sesión de SQLAlchemy
engine = create_engine(sqlite_db_path)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Lee el archivo Excel en un DataFrame de pandas
df = pd.read_excel(excel_file, sheet_name='English')

# Convierte las columnas de fecha del DataFrame a datetime de pandas
df['DATE'] = pd.to_datetime(df['DATE'], format='%d/%m/%Y %I:%M:%S %p')

# Define una función para importar datos a la base de datos
def import_data_to_db(session, dataframe):
    for index, row in dataframe.iterrows():
        estudio = Base_Estudio(
            Ingles=row['ENGLISH'],
            Espanol=row['SPANISH'],
            Fonetica=row.get('Fonetica', None),  # Usa None para representar un valor nulo
            Pronunciacion_simple=row.get('Pronunciacion_simple', None),  # Usa None para representar un valor nulo
            Nivel=row['LEVEL'],
            Categoria=row['Categoria'],
            Tipo_de_repaso=row['Tipo_de_repaso'],
            Date=row['DATE']
        )
        session.add(estudio)
    session.commit()

# Ejecuta la función de importación dentro de un contexto de sesión
def main():
    with SessionLocal() as session:
        import_data_to_db(session, df)

if __name__ == "__main__":
    main()
