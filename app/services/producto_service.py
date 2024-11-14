from app.models import Producto
from app.producto_repository import ProductoRepository
from app import cache
from flask import abort

repository = ProductoRepository()

class ProductoService:

    def find(self, id: int) -> Producto:
        result = None
        if id is not None:
            result = cache.get(f"producto_{id}")

            if result is not None:
                print(f"Producto {id} obtenido del caché")  # Agregamos un mensaje de depuración
            else:
                print(f"Producto {id} no está en el caché. Consultando el repositorio...")
                result = repository.find(id)

                if result is None:
                    abort(404, description="Product not found")
                cache.set(f"producto_{id}", result, timeout=50)
                
        return result