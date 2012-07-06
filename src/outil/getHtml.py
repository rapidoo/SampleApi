'''
Created on 5 juil. 2012

@author: flebris
'''
import simplejson
import getApi

class ParseCanada:
    
    def get(self, reponse): 
        '''
        Retourne un flux html mis en forme a partir d'un json
        '''
        
        url1 = '<!DOCTYPE html><html><head></head><body><h1>Reponses : </h1>'
        url2 = '</body></html>'
    
        fluxHtml = url1 + '<ul>'
                
        data = simplejson.loads(reponse)
        
        for bloc in data['listings']:
            
            idBloc = bloc['id']
            name = bloc['name']
            adress = bloc['address']
            prov = adress['prov']
            street = adress['street']
            city = adress['city']
            detail = simplejson.loads(getApi.Canada().detail(idBloc, name, prov))
            numero = self.getNumero(detail)
            #numero = getApi.Canada().detail(idBloc, name, prov)
            fluxHtml = fluxHtml + '<li>' + name +'</br><ul>'
            fluxHtml = fluxHtml + '<li>' + street + '</li><li>' + city + '</li>' 
            fluxHtml = fluxHtml + '<li>' + numero + '</li>' 
            fluxHtml = fluxHtml  + '</ul>'
          
        fluxHtml = fluxHtml + url2
        
        return fluxHtml


    def getNumero(self, detail):
        
        numero = ''
        phones = detail['phones']
        
        for phone in phones:
            numero = phone['dispNum'] 
             
        return numero
        
  