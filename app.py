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
        x = web.input(myfile={})
        filedir = './images'
        if 'myfile' in x:
            filepath=x.myfile.filename.replace('\\','/')
            filename=filepath.split('/')[-1]
            fout = open(filedir +'/'+ filename,'w')
            fout.write(x.myfile.file.read())
            fout.close()
        raise web.seeother('/upload')


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
