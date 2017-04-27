import web
from urls import urls

#web.config.debug = False
render = web.template.render('templates/')


class index:
    def GET(self, name=None):
        return render.index(name)


class Upload:
    def GET(self):
        web.header("Content-Type", "text/html; charset=utf-8")
        return render.upload()

    def POST(self):
        pass


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
