from app.models import Producto
from app.producto_repository import ProductoRepository
from flask import abort

repository = ProductoRepository()

class ProductoService:

    def find(self, id: int) -> Producto:
        product = repository.find(id)
        if product is None:
            abort(404, description="Product not found")
        return product