'''
Created on 5 juil. 2012

@author: flebris
'''
import simplejson

class getHtml:
    
    def get(self, reponse): 
        '''
        Retourne un flux html mis en forme a partir d'un json
        '''
        
        url1 = '<!DOCTYPE html><html><head></head><body><h1>Reponses : </h1>'
        url2 = '</body></html>'
    
        fluxHtml = url1 + '<ul>'
                
        data = simplejson.loads(reponse)
        
        for bloc in data['listings']:
        
            name = bloc['name']
            fluxHtml = fluxHtml + '<li>' + name + '</li>'
        
        fluxHtml = fluxHtml + url2
        
        return fluxHtml

  