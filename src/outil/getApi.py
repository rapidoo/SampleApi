'''
Created on 3 juil. 2012

@author: flebris
'''
from google.appengine.api import urlfetch 

class getApi:
    
    url1 = 'http://api.sandbox.yellowapi.com/FindBusiness/?pg=1&what='
    url2 = '&lang=en&where='
    url3 = '&pgLen=40&fmt=JSON&UID=1&apikey=6vvstrbxxpd6ckcm24w6u3jd'
   
 


    def gfetch(self, what, where): 
    
        urlHttp = self.url1 + what + self.url2 + where + self.url3
      
        response = urlfetch.fetch(url=urlHttp, payload=None, method='GET', headers={}, allow_truncated=False, follow_redirects=True, deadline=None)
        
        if response.status_code == 200 :
            return response.content
        else:
            return "Erreur dans interogation API !!!"


   