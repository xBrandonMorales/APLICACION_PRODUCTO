import web
"""Importamos la clase ModeloIndex del modelo_index.py"""
from mvc.models.modelo_index import ModeloIndex

reander = web.template.render('mvc/views/')

m_index = ModeloIndex() # Se crea objeto de la clase ModeloIndex

class index:
    def GET(self):
        try
            resultado = m_index.consultaProductos()
            return render.index(resultado)
        exept Excepcion as e:
            print("Error 101 - index {e.args}")
            return "Ups algo salio mal"