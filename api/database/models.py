from typing import List
from api.database.database import Base
from sqlalchemy import Column, Integer, String, Float

class Prezunic(Base):
    __tablename__ = "item_prezunic"

    id: int = Column(Integer, primary_key=True, index=True)
    nome: str = Column(String(200), nullable=True)
    preco: float = Column(Float, nullable=True)
    # fonte: str = Column(String(200), nullable=False)

class MercadoLivre(Base):
    __tablename__ = "item_mercadolivre"

    id: int = Column(Integer, primary_key=True, index=True)
    nome: str = Column(String(200), nullable=True)
    preco: float = Column(Float, nullable=True)
    # fonte: str = Column(String(200), nullable=False)

class PaodeAcucar(Base):
    __tablename__ = "item_paodeacucar"

    id: int = Column(Integer, primary_key=True, index=True)
    nome: str = Column(String(200), nullable=True)
    preco: float = Column(Float, nullable=True)
    # fonte: str = Column(String(200), nullable=False)    
