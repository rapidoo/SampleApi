'''
Created on 3 juil. 2012

@author: flebris
'''
import httplib2
        
url = 'http://api.sandbox.yellowapi.com/FindBusiness/?pg=1&what=resto&lang=en&where=toronto&pgLen=40&fmt=JSON&UID=1&apikey=6vvstrbxxpd6ckcm24w6u3jd'
   
http = httplib2.Http()

response, content = http.request(url, "GET")

print response


