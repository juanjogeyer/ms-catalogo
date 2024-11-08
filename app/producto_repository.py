from app.models import Producto
from app import db

class ProductoRepository:

    #Obtiene todos los productos activados
    def find(self, id: int) -> Producto:
        result = None
        if id is not None:
            result = db.session.query(Producto).filter(Producto.id == id, Producto.activado == True).one_or_none()
        return result