'''
Created on 3 juil. 2012

@author: flebris
'''
import utils


class Canada:
    
    urlListe1 = 'http://api.sandbox.yellowapi.com/FindBusiness/?pg=1&what='
    urlListe2 = '&lang=en&where='
    urlListe3 = '&pgLen=5&fmt=JSON&UID=1&apikey=6vvstrbxxpd6ckcm24w6u3jd'

    urlDetail1 = 'http://api.yellowapi.com/GetBusinessDetails/?prov='
    urlDetail2 = '&bus-name='
    urlDetail3 = '&listingId='
    urlDetail4 = '&fmt=JSON&apikey=a1s2d3f4g5h6j7k8l9k6j5j4&UID=1'




    def listeReponse(self, what, where): 
    
        urlHttp = self.urlListe1 + what + self.urlListe2 + where + self.urlListe3
        
        retour = utils.fetchCache(urlHttp)
    
        return retour

    def detail(self, idBloc, name, prov): 
    
        name = name.replace(' ','-') 
    
        urlHttp = self.urlDetail1 + prov + self.urlDetail2 + name + self.urlDetail3 + idBloc + self.urlDetail4
      
        return utils.fetchCache(urlHttp)


class France:
    
    urlListe1 = 'http://api.test.pagesjaunes.fr/pro/find.json?what='
    urlListe2 = '&where='
    urlListe3 = '&app_id=f9cc727a&app_key=62aa71dd3a03a981d81cf3afee3470a4'
    

    def listeReponse(self, what, where): 
    
        urlHttp = self.urlListe1 + what + self.urlListe2 + where + self.urlListe3
        
        retour = utils.fetchCache(urlHttp)
    
        return retour



  