import web
from urls import urls
import cgi
import urllib
import urllib2
import json
import subprocess
#import requests
#import simplejson as json

# Maximum input we will accept when REQUEST_METHOD is POST
# 0 ==> unlimited input
#cgi.maxlen = 1 * 1024 * 1024 #10MB

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
    upload_id = 0

    def GET(self):
        web.header("Content-Type", "text/html; charset=utf-8")
        return render.upload()

#    def POST(self):
#        Upload.upload_id += 1
#        try:
#            images =  web.input()
#        except ValueError:
#            return "File too large"
        #return images.keys()
        #return images
        #return json.dumps({k:images[k] for k in images.keys()})
        #data_string = json.dumps({k:images[k] for k in images.keys()})
        #data_string = json.dumps({k:images[k].enconde('utf-8').strip() for k in images.keys()})

#        data_string = {k:images[k] for k in images.keys()}
#        data_string.update({'Id': str(Upload.upload_id)})
#        encoded_args = urllib.urlencode(data_string)
#        url = 'http://127.0.0.1:3030/sever/'
#        return urllib2.urlopen(url, encoded_args).read()

    def POST(self):
        Upload.upload_id += 1

        #images = dict(web.input())
        images = web.input()
        #url = 'http://127.0.0.1:3030/sever/'
        filedir = '/tmp'
        data_string = {"Id": str(Upload.upload_id)}
        #filedir = './images'

        #if 'myfile' in x:
        #    filepath=x.myfile.filename.replace('\\','/')
        #    filename=filepath.split('/')[-1]
        #    fout = open(filedir +'/'+ filename,'w')
        #    fout.write(x.myfile.file.read())
        #    fout.close()
        #raise web.seeother('/upload')
        #return dir(images)
        #return dir(images.Tallo1)
        for counter, value in enumerate(images, 1):
            filename = "tallo" + str(counter) + "-" + str(Upload.upload_id)
            filepath = filedir + "/" + filename
            #print "FILEPATH:", filepath
            with open(filepath, r'w') as f:
                f.write(images[value])
            #data_string.update("Tallo" + str(counter), filepath)
            data_string.update({"Tallo" + str(counter): filepath})
            #return images[value]
        #json_data = json.dumps(data_string)
        #print "JSON:", json_data
        print "DRAW:", data_string
        #respond = requests.post(url, json=json_data)
        #print respond.status_code
        encoded_args = urllib.urlencode(data_string)
        print "ENCODED: ", encoded_args
        #return encoded_args 
        #raise web.seeother('/severity?' + encoded_args)
        #raise web.seeother('/severity?f=1')
        raise web.seeother('/severity?' + encoded_args)

class Severity:
    def GET(self):
        json_data = json.dumps(web.input())
        url = 'http://127.0.0.1:3030/sever/'
        #respond = requests.post(url, json=json_data)
        #print "RESPOND:", respond.status_code
        #return respond.json()
        output = subprocess.check_output(['curl', '-XPOST', url, '-d', str(json_data)])
        #output = '{ "id": "1",\
        #        "porcentaje": "nulo",\
        #        "mensaje":[{\
        #        "medidas": "preventivas",\
        #        "tratamiento": "utilice fungicidas protectantes y practicas\
        #        culturales."\
        #        }]}'
        json_data = json.loads(output)
        print(json.dumps(json_data, indent=4))
        return render.severity(json_data)


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
else:
    app = web.application(urls, globals())
    application = app.wsgifunc()
