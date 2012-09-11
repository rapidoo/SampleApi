'''
Created on 10 juil. 2012

@author: flebris
'''
from google.appengine.api import memcache
from google.appengine.api import urlfetch


def fetchCache(urlHttp):

    client = memcache.Client()
    response = client.get(urlHttp)
    if response is not None:
        retour = response
    else:
        response = fetchUrl(urlHttp)
        client.add(urlHttp, response, 3600)
        retour = response
    return retour

def fetchUrl(urlHttp):
        
    response = urlfetch.fetch(url=urlHttp, payload=None, method='GET', headers={}, allow_truncated=False, follow_redirects=True, deadline=None)
        
    if response.status_code == 200 :
        return response.content
    else:
        return "Erreur dans interogation Liste Reponse !!!"


    
    