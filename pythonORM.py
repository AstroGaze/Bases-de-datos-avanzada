import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Country
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_NAME = 'master'

# Crear la conexión a la base de datos
engine = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}')

# Verificar la conexión a la base de datos
try:
    connection = engine.connect()
    print("Conexion a la base de datos establecida correctamente.")
    connection.close()
except Exception as e:
    print(f"Error al conectar a la base de datos: {e}")

# Crear una sesión
Session = sessionmaker(bind=engine)
session = Session()

def run_tests(session):
    print("Iniciando pruebas...")
    
    # Prueba de inserción
    add_country(session, 'TE', 'Test Country', 1)
    
    # Prueba de consulta
    results = query_countries(session, country_id='BR')
    print("Resultado de la consulta:", results)
    
    # Prueba de actualización
    update_country(session, 'TE', country_name='Updated Test Country')
    results = query_countries(session, country_id='TE')
    print("Resultado despues de la actualizacion:", results)
    
    # Prueba de eliminacion
    """ delete_country(session, 'TE')
    results = query_countries(session, country_id='TE')
    print("Resultado después de la eliminacion:", results) """
    
    print("Pruebas completadas.")

if __name__ == "__main__":
    from CRUD import add_country, query_countries, update_country, delete_country
    run_tests(session)