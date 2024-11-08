from dataclasses import dataclass
from app import db

@dataclass(init=False, repr=True, eq=True)
class Producto(db.Model):
    __tablename__ = 'catalogo'
    
    id: int = db.Column(db.Integer, primary_key=True)
    nombre: str = db.Column(db.String(100), nullable=False)
    precio: float = db.Column(db.Float, nullable=False)
    activado: bool = db.Column(db.Boolean, default=True)