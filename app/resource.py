from flask import Blueprint
from app.mapping import ProductoSchema, ResponseSchema
from app.services.response_message import ResponseBuilder
from app.services import ProductoService

catalogo = Blueprint('catalogo', __name__)

producto_schema = ProductoSchema()
response_schema = ResponseSchema()
producto_service = ProductoService()

@catalogo.route('/catalogo/productos/<int:id>', methods=['GET'])
def get_producto(id: int):
    response_builder = ResponseBuilder()
    data = producto_schema.dump(producto_service.find(id))
    if data:
        response_builder.add_message("Producto encontrado").add_status_code(200).add_data(data)
        return response_schema.dump(response_builder.build()), 200
    else:
        response_builder.add_message("Producto NO encontrado").add_status_code(404)
        return response_schema.dump(response_builder.build()), 404