
import web
import base64
from ..models.modelo_productos import ModeloProductos


PRODUCTO = ModeloProductos()


render = web.template.render('mvc/views/', base='layout')


class ActualizarProductos:

    def GET(self, idProducto):
        """
            Función que se encarga de renderizar la vista de actualizar_productos recibiendo como parámetro
            el identificador del producto
        """
        
        try:
            
            producto = PRODUCTO.detalleProductos(idProducto)
            print(producto)
            
            return render.actualizar_productos(producto)
        
        except Exception as error:
            print(f'Ocurrió un error {error} - 105 | Controlador')
            return "Ocurrió un error"

    def POST(self, idProducto):
        """
            Función que se encarga de enviar datos obteniendolos de un formulario, en este caso son datos para
            actualizar un producto en la base de datos
        """
        
        try:
            
            entrada = web.input(imagen = {})

            
            if entrada['imagen'].value:
                extension = entrada['imagen'].filename.split('.')
                extension = extension[1]

           
            if entrada and idProducto == entrada.producto:
                producto =  {
                    "producto": entrada.producto,
                    "nombre":entrada.nombre_producto,
                    "descripcion":entrada.descripcion,
                    "imagen": base64.b64encode(entrada['imagen'].file.read()).decode('ascii'),
                    "extension": extension,
                    "precio":entrada.precio,
                    "existencia":entrada.existencia
                }
                
                resultado = PRODUCTO.actualizarProductos(producto)
            
            if resultado:
                web.seeother("/")
            else:
                return render.actualizar_productos(entrada.producto)

        
        except Exception as error:
            print(f'Ocurrió un error {error} - 105_2 | Controlador')
            return "Oucrrió un error"