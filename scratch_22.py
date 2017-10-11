

import requests
consulta = 'red hot chili peppers, pulp fiction'

parametros = {'k':'286940-DevFSens-0KCM0XSU','q': consulta }

url='https://tastedive.com/api/similar'
respuesta = requests.get(url, params=parametros)

print respuesta.url

json_object_respuesta = respuesta.json()

print json_object_respuesta

class The_Dates(object):
    def __init__(self,data_object):
        self.info=data_object
        self.name=data_object['name']
        self.type=data_object['type']

