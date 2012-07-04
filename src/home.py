from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
import outil.getApi



class MainPage(webapp.RequestHandler):
    
    def get(self):
        
        url1 = '<!DOCTYPE html><html><head></head><body><h1>Saisir votre requetre</h1><form name="input" action="/getBusiness" method="get">'
        url2 = 'What: <input type="text" name="what" />Where: <input type="text" name="where" /><input type="submit" value="Submit" /></form></body></html>'

        reponse = url1 + url2
        
        #requete = outil.getApi.getApi()
        #reponse = requete.get('resto', 'toronto')
        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write('' + reponse )


class BrowseHandler(webapp.RequestHandler):

    def get(self, what, where):
        
        requete = outil.getApi.getApi()
        reponse = requete.get(what, where)
        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write('' + reponse )



class getBusinessHandler(webapp.RequestHandler):

    def post(self):
        
        requete = outil.getApi.getApi()
        
        what = self.request.get('what')
        where = self.request.get('where')
        
        print "what = " + what
        print "where = " + where 
        
        reponse = what
        #reponse = requete.get(what, where)
        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write('' + reponse )

        

application = webapp.WSGIApplication([('/', MainPage),
                                      (r'/getBusinessRest/(.*)/(.*)', BrowseHandler),
                                      (r'/getBusiness', getBusinessHandler)
                                     ],
                                     debug=True)
def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
