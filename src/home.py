from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from outil import getApi
from outil import getHtml



class MainPage(webapp.RequestHandler):
    
    def get(self):
        
        url1 = '<!DOCTYPE html><html><head></head><body><h1>Saisir votre requete sur API Canada</h1>'
        url2 = '<form name="input" action="/getBusiness" method="get">'
        url3 = 'What: <input type="text" name="what" />Where: <input type="text" name="where" /><input type="submit" value="Submit" /></form></body></html>'
        reponse = url1 + url2 + url3
        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write('' + reponse )


class getBusinessRestHandler(webapp.RequestHandler):

    def get(self, what, where):
        
        requete = getApi.Canada()
        reponse = requete.listeReponse(what, where)
    
        html = getHtml.ParseCanada() 
        fluxHtml = html.get(reponse) 

        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write('' + fluxHtml )


class getBusinessHandler(webapp.RequestHandler):

    def get(self):
        
        what = self.request.get("what")
        where = self.request.get("where")
        
        requete = getApi.Canada()
        reponse = requete.listeReponse(what, where)
        
        html = getHtml.ParseCanada() 
        fluxHtml = html.get(reponse)

        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write(fluxHtml)

        

application = webapp.WSGIApplication([('/', MainPage),
                                      (r'/getBusinessRest/(.*)/(.*)', getBusinessRestHandler),
                                      (r'/getBusiness', getBusinessHandler)
                                     ],
                                     debug=True)
def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
