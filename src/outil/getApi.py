'''
Created on 3 juil. 2012

@author: flebris
'''
import httplib2
   

class getApi:
    
    url1 = 'http://api.sandbox.yellowapi.com/FindBusiness/?pg=1&what='
    url2 = '&lang=en&where='
    url3 = '&pgLen=40&fmt=JSON&UID=1&apikey=6vvstrbxxpd6ckcm24w6u3jd'
   
    def get(self, what, where): 
    
        url = self.url1 + what + self.url2 + where + self.url3
        
        http = httplib2.Http()

        response, content = http.request(url, "GET")

        if response.status == 200 :
            return content
        else:
            return "{error !!!}"



   