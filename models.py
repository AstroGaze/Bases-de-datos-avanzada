from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Country(Base):
    __tablename__ = 'countries'

    country_id = Column(String(2), primary_key=True)
    country_name = Column(String(40))
    region_id = Column(Integer)

    def __repr__(self):
        return f"<Country(country_id='{self.country_id}', country_name='{self.country_name}', region_id={self.region_id})>"