import unittest, os
from app import create_app, db
from app.models import Producto
from app.services import ProductoService

producto_service = ProductoService()

class CatalogoTestCase(unittest.TestCase):
    
    def setUp(self):
        # Producto
        self.NOMBRE_TEST = 'Producto 1'
        self.PRECIO_TEST = 3500
        self.ACTIVADO_TEST = True
        
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_producto(self):
        producto = self.__get_producto()

        self.assertEqual(producto.nombre, self.NOMBRE_TEST)
        self.assertEqual(producto.precio, self.PRECIO_TEST)
        self.assertEqual(producto.activado, self.ACTIVADO_TEST)

    def test_producto_find(self):
        producto = self.__get_producto()
        db.session.add(producto)
        db.session.commit()

        producto_find = producto_service.find(1)
        self.assertIsNotNone(producto_find)
        self.assertEqual(producto_find.id, producto.id)
        self.assertEqual(producto_find.nombre, producto.nombre)

    def __get_producto(self) -> Producto:
        producto = Producto()
        producto.nombre = self.NOMBRE_TEST
        producto.precio = self.PRECIO_TEST
        producto.activado = self.ACTIVADO_TEST
        return producto

if __name__ == '__main__':
    unittest.main()