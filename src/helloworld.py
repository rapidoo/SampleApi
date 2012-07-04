from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
import outil.getApi


class MainPage(webapp.RequestHandler):
    
    def get(self):
        
        requete = outil.getApi.getApi()
        reponse = requete.get('resto', 'toronto')
        
        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write('' + reponse )


application = webapp.WSGIApplication([('/', MainPage)], debug=True)


def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
