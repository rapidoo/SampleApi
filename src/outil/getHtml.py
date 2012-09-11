'''
Created on 5 juil. 2012

@author: flebris
'''
import json
import getApi


class site:
    
    def getHome(self):
        
        header = '<!DOCTYPE html><html><head></head><body>'
        
        reponse = header
        
        url1 = '<h1>Saisir votre requete sur API Pro Canada</h1>'
        url2 = '<form name="input" action="/getBusiness" method="get">'
        url3 = 'What: <input type="text" name="what" />Where: <input type="text" name="where" /><input type="submit" value="Submit" /></form></body></html>'
        
        reponse = reponse + url1 + url2 + url3
        
        
        url11 = '<h1>Saisir votre requete sur API Pro PagesJaunes</h1>'
        url12 = '<form name="input" action="/getPro" method="get">'
        url13 = 'What: <input type="text" name="what" />Where: <input type="text" name="where" /><input type="submit" value="Submit" /></form>'
        
        reponse = reponse + url11 + url12 + url13
        
        close = '</body></html>'
        
        reponse = reponse + close
        
        return reponse

class parseCanada:
    
    def get(self, reponse): 
        '''
        Retourne un flux html mis en forme a partir d'un json
        '''
        
        url1 = '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"></head><body><h1>Reponses : </h1>'
        url2 = '</body></html>'

        idBloc = ''
        name = ''
        adress = ''
        prov = ''
        street = ''
        city = ''
        numero=''

    
        fluxHtml = url1 + '<ul>'
        
        try:
                    
            data = json.loads(reponse)
            
            for bloc in data['listings']:
                
                idBloc = bloc['id']
                name = bloc['name']
                adress = bloc['address']
                prov = adress['prov']
                if(prov==''):
                    prov='Canada'
                street = adress['street']
                city = adress['city']
                numero=''
                try:
                    detail = getApi.Canada().detail(idBloc, name, prov)
                    detail = json.loads(detail)
                    numero = self.getNumero(detail)
                except Exception:
                    numero = ''
                        
                fluxHtml = fluxHtml + '<li>' + name +'</br><ul>'
                fluxHtml = fluxHtml + '<li>' + street + '</li><li>' + city + '</li>' 
                fluxHtml = fluxHtml + '<li>' + numero + '</li>' 
                fluxHtml = fluxHtml  + '</ul>'
              
                fluxHtml = fluxHtml + url2
        
            return fluxHtml
            
        except Exception:
                
            fluxHtml = url1 + 'Exception !!!'
            return fluxHtml    



    def getNumero(self, detail):
        
        numero = ''
        phones = detail['phones']
        
        for phone in phones:
            numero = phone['dispNum'] 
             
        return numero
        
class parseFrance:
    
    def get(self, reponse): 
        '''
        Retourne un flux html mis en forme a partir d'un json
        '''
        
        url1 = '<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"></head><body><h1>Reponses : </h1>'
        url2 = '</body></html>'
       
        name = ''
        description=''
        street = ''
        city = ''
        numero=''

        fluxHtml = url1 + '<ul>'
        
                   
        data = json.loads(reponse)
        
        listings = data['search_results']
        
        for bloc in listings['listings']:
            
            name = bloc['merchant_name']
            description = bloc['description']
            
            fluxHtml = fluxHtml + '<li>' + name + '</br><ul>'
            fluxHtml = fluxHtml + '<li>' + description + '</li>'
            
            inscription = bloc['inscriptions']
            fluxHtml = fluxHtml + '<li>' + inscription['adress_street'] + '</li>'
            
            contact = inscription['contact_info']
            
           # tel = contact["contact_type".encode('utf-8')]
            #fluxHtml = fluxHtml + '<li>' + tel + '</li>'
            
            
            fluxHtml = fluxHtml  + '</ul>'
           
         #   categorie = bloc['categories']['category_name']
                
            #fluxHtml = fluxHtml + '<li>' + categorie['category_name'] + '</li>'
            
            
            #fluxHtml = fluxHtml + '<li>' + categorie['category_name'] + '</li>'
            
       
            
            
            
      #  for categorie in listings['categories']:
       #      toto = 'fred'
             
       #     for inscription in listing['inscriptions']:
                
        #        
           #     street = inscription['adress_street']
         #       city = inscription['adress_city']
             
         #       fluxHtml = fluxHtml + '<li>' + street + '</li><li>' + city + '</li>' 
               
         #       for contact in inscription['contact_info']:
                    
         #           numero = contact['contact_value']
                    
         #           fluxHtml = fluxHtml + '<li>' + numero + '</li>' 
            
        fluxHtml = fluxHtml  + '</ul>'
          
        fluxHtml = fluxHtml + url2
    
        return fluxHtml
            



 
        