'''
Created on 3 juil. 2012

@author: flebris
'''
from google.appengine.api import urlfetch
from google.appengine.api import memcache

class Canada:
    
    urlListe1 = 'http://api.sandbox.yellowapi.com/FindBusiness/?pg=1&what='
    urlListe2 = '&lang=en&where='
    urlListe3 = '&pgLen=5&fmt=JSON&UID=1&apikey=6vvstrbxxpd6ckcm24w6u3jd'
   

    urlDetail1 = 'http://api.yellowapi.com/GetBusinessDetails/?prov='
    urlDetail2 = '&bus-name='
    urlDetail3 = '&listingId='
    urlDetail4 = '&fmt=JSON&apikey=a1s2d3f4g5h6j7k8l9k6j5j4&UID=1'

    client = memcache.Client()


    def fetchCache(self, urlHttp):
        response = self.client.get(urlHttp)
        if response is not None:
            retour = response
        else:
            response = self.fetchUrl(urlHttp)
            self.client.add(urlHttp, response, 3600)
            retour = response
        return retour

    def listeReponse(self, what, where): 
    
        urlHttp = self.urlListe1 + what + self.urlListe2 + where + self.urlListe3
        
        retour = self.fetchCache(urlHttp)
    
        return retour

    def detail(self, idBloc, name, prov): 
    
        name = name.replace(' ','-') 
    
        urlHttp = self.urlDetail1 + prov + self.urlDetail2 + name + self.urlDetail3 + idBloc + self.urlDetail4
      
        return self.fetchCache(urlHttp)


    def fetchUrl(self, urlHttp):
        
        response = urlfetch.fetch(url=urlHttp, payload=None, method='GET', headers={}, allow_truncated=False, follow_redirects=True, deadline=None)
        
        if response.status_code == 200 :
            return response.content
        else:
            return "Erreur dans interogation Liste Reponse !!!"
