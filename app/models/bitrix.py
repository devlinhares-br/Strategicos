from os import getenv
import requests

class Bitrix24():
    def __init__(self) -> None:
        self.__BASE_URL = getenv('BASE_URL')
        self.__METHODS = {
            'update': 'crm.item.update',
            'list': 'crm.item.list',
            'get': 'crm.item.get'
        }
    
    def request(self, method:str, json:dict) -> requests:
        url = f'{self.__BASE_URL}{method}'
        return requests.post(url, json=json)
    
    def update(self, data:dict, entity_type, entity_id:int)-> requests:
        json = {
            'entityTypeId': entity_type,
            'id': entity_id,
            'fields': data
        }
        return self.request(self.__METHODS['update'], json)
    
    def list(self, data:dict, entity_id:int)-> requests:
        json = {
            'entityTypeId': entity_id,
            'filter': data
        }
        return self.request(self.__METHODS['list'], json)
    
    def get(self, id:int, entity_id:int)-> requests:
        json = {
            'entityTypeId': entity_id,
            'id': id
        }
        return self.request(self.__METHODS['get'], json)