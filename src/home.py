from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from outil import getApi
from outil import getHtml
from outil import getWhere


class MainPage(webapp.RequestHandler):
    
    def get(self):
        
        reponse = getHtml.site().getHome()
       
        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write(reponse )


class getBusinessRestHandler(webapp.RequestHandler):

    def get(self, what, where):
        
        reponse = getApi.Canada().listeReponse(what, where)
    
        fluxHtml = getHtml.parseCanada().get(reponse) 

        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write(fluxHtml )


class getBusinessHandler(webapp.RequestHandler):

    def get(self):
        
        what = self.request.get("what")
        where = self.request.get("where")
        
        #On valide le ou
        gwhere = getWhere.getCountry(where)
        
        if(gwhere != 'Canada'):
            fluxHtml = 'Ce pays n est pas encore supporte'
        else:
            reponse = getApi.Canada().listeReponse(what, where)
            
            fluxHtml = getHtml.parseCanada().get(reponse)

        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write(fluxHtml)
#        self.response.out.write(gwhere)

class getProHandler(webapp.RequestHandler):

    def get(self):
        
        what = self.request.get("what")
        where = self.request.get("where")
        
       
        reponse = getApi.France().listeReponse(what, where)
            
        fluxHtml = getHtml.parseFrance().get(reponse)

        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write(fluxHtml)

        

application = webapp.WSGIApplication([('/', MainPage),
                                      (r'/getBusinessRest/(.*)/(.*)', getBusinessRestHandler),
                                      (r'/getBusiness', getBusinessHandler),
                                      (r'/getPro', getProHandler)
                                     ],
                                     debug=True)
def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
