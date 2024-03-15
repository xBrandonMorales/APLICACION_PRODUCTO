
import web
from ..models.modelo_productos import ModeloProductos


PRODUCTO = ModeloProductos()


render = web.template.render('mvc/views/', base='layout')


class ListaProductos:

    def GET(self):
        """
            Función que se encarga de renderizar la vista de lista_productos enviando como parámetro los productos
            obtenidos de la función de listaProductos del módelo
        """
        
        try:
            
            productos = PRODUCTO.listaProductos()
            
            return render.lista_productos(productos)
        
        except Exception as error:
            print(f"Ocurrió un error {error} - 101 | Controlador")
            return "Ocurrió un error"

    def POST(self):
        """
            Función que se encarga de enviar datos ingresados en formularios de esta vista, principalmente utilizada
            para buscar los productos
        """
        
        try:
            
            entrada = web.input()
            producto_buscado = entrada.nombre
            
            if entrada and producto_buscado:
                respuesta = PRODUCTO.buscarProductos(producto_buscado)
           
            if respuesta:
                return render.lista_productos(respuesta)
            else:
                web.seeother("/")
        
        except Exception as error:
            print(f"Ocurrió un error {error} - 101_2 | Controlador")
            return "Ocurrió un error"