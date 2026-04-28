from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Venta(Base):
    __tablename__ = "ventas"

    id = Column(Integer, primary_key=True)
    producto = Column(String)
    cantidad = Column(Integer)
    precio = Column(Integer)