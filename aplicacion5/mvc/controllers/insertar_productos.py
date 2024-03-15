
import web
import base64
from ..models.modelo_productos import ModeloProductos


PRODUCTO = ModeloProductos()


render = web.template.render('mvc/views/', base='layout')


class InsertarProductos:

    def GET(self):
        """
            Función que se encarga de renderizar la vista de insertar_productos, el cuál es un formulario
            para obtener los datos
        """
        
        try:
            
            return render.insertar_productos()
        
        except Exception as error:
            print(f'Ocurrió un error: {error} - 104 | Controlador')
            return "Ocurrió un error"

    def POST(self):
        """
            Función que se encarga de enviar datos, en este caso obtiene los datos del formulario para insertar
            productos
        """
        
        try:
            
            entrada = web.input(imagen = {})
            
            extension = entrada['imagen'].filename.split('.')
            
            if entrada:
                producto =  {
                    "nombre":entrada.nombre_producto,
                    "descripcion":entrada.descripcion,
                    "imagen": base64.b64encode(entrada['imagen'].file.read()).decode('ascii'),
                    "extension": extension[1],
                    "precio":entrada.precio,
                    "existencia":entrada.existencia
                }
                
                resultado = PRODUCTO.insertarProductos(producto)
            
            if resultado:
                web.seeother("/")
            else:
                return render.insertar_productos()
        
        except Exception as error:
            print(f"Ocurrió un error: {error} - 104_2 | Controlador")
            return "Ocurrió un error"