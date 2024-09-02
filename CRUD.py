from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from models import Country

def query_countries(session, **kwargs):
    """Consulta países basado en criterios específicos."""
    return session.query(Country).filter_by(**kwargs).all()

def add_country(session, country_id, country_name, region_id):
    """Agrega un nuevo país a la base de datos."""
    new_country = Country(country_id=country_id, country_name=country_name, region_id=region_id)
    session.add(new_country)
    try:
        session.commit()
        print(f"Pais '{country_name}' agregado exitosamente.")
    except IntegrityError:
        session.rollback()
        print(f"Error: El pais con ID '{country_id}' ya existe.")

def update_country(session, country_id, **kwargs): 
    """Actualiza la información de un país existente."""
    country = session.query(Country).filter_by(country_id=country_id).first()
    if country:
        for key, value in kwargs.items():
            setattr(country, key, value)
        session.commit()
        print(f"Pais '{country.country_name}' actualizado exitosamente.")
    else:
        print(f"Error: No se encontróo un país con ID '{country_id}'.")

def delete_country(session, country_id):
    """Elimina un país de la base de datos."""
    country = session.query(Country).filter_by(country_id=country_id).first()
    if country:
        session.delete(country)
        session.commit()
        print(f"Pais '{country.country_name}' eliminado exitosamente.")
    else:
        print(f"Error: No se encontró un país con ID '{country_id}'.")