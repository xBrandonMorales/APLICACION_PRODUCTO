import web 

urls = (
    "/", "hello",
    "/pagina2", "hola"  # Agrega una coma aquí
)

app = web.application(urls, globals())

class hello:
    def GET(self):
        return 'Hola Pagina1'

class hola:
    def GET(self):
        return 'Hola Pagina2'

if _name_ == "_main_":
    app.run()