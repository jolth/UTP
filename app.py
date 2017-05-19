import web
from urls import urls
import cgi

# Maximum input we will accept when REQUEST_METHOD is POST
# 0 ==> unlimited input
cgi.maxlen = 10 * 1024 * 1024 #10MB

#web.config.debug = False
render = web.template.render('templates/', base='layout')
#render = web.template.render('templates/')


class home:
    def GET(self):
        return render.home()

class Contact:
    def GET(self):
        return render.contact()

class Help:
    def GET(self):
        return render.help()

class Upload:
    def GET(self):
        web.header("Content-Type", "text/html; charset=utf-8")
        return render.upload()

    def POST(self):
        try:
            img =  web.input(images={})
        except ValueError:
            return "File too large"
        print img.keys

    #def POST(self):
    #    x = web.input(myfile={})
    #    filedir = './images'
    #    if 'myfile' in x:
    #        filepath=x.myfile.filename.replace('\\','/')
    #        filename=filepath.split('/')[-1]
    #        fout = open(filedir +'/'+ filename,'w')
    #        fout.write(x.myfile.file.read())
    #        fout.close()
    #    raise web.seeother('/upload')


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
