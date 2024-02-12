"""Framework web.py"""
import web

urls=(
    "/", "mvc,controllers.index.Index"
)

app = web.application(urls, globals())

class hello:
    def GET(self, name):
        if not name:
            name = 'World'
        return 'Hola, ' + name + '!'

if __name__ == "__main__":
    web.config,debug = False
    app.run()
    