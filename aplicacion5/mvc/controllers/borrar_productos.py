
import web
from ..models.modelo_productos import ModeloProductos


PRODUCTO = ModeloProductos()


render = web.template.render('mvc/views/', base='layout')


class BorrarProductos:

    def GET(self, idProducto):
        """
            Función que se encarga de renderizar la vista de borrar_productos utilizando el identificador
            del producto como parámetro
        """
        
        try:
            
            producto = PRODUCTO.detalleProductos(idProducto)
            
            return render.borrar_productos(producto)
        
        except Exception as error:
            print(f'Ocurrió un error: {error} - 106 | Controlador')
            return "Ocurrió un error"

    def POST(self, id_producto):
        """
            Función que se encarga de enviar datos que se ingresan mediante el formulario correspondiente
            esto principalmente para eliminar datos de la base de datos
        """
        
        try:
            
            form = web.input()
            
            if id_producto == form.producto:
                result = PRODUCTO.borrarProductos(id_producto)
            
            if result:
                web.seeother('/')
            else:
                return render.borrar_productos(form.producto)
        
        except Exception as error:
            print(f"Ocurrió un error: {error} - 106_2 | Controlador")
            return "Ocurrió un error"