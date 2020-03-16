# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import pandas as pd
import json
from datetime import datetime
from graphqlclient import GraphQLClient
import requests
import os.path
import uuid



class RealmToken:
    def __init__(self, url, path, filename, username, password):
        self._username = username
        self._password = password
        self._filename = filename
        self._url = url
        self._path = path
        self._reset()
        self._load()

    def _reset(self):
        self._token = None
        self._expires = None
        self._expired = None

    def _load(self):
        if os.path.isfile(self._filename):
            with open(self._filename) as f:
                data = json.load(f)
                self._token = data['token']
                self._expires = data['expires']

    def _check_expired(self):
        if self._expires:
            self._expired = datetime.fromtimestamp(self._expires) < datetime.now()

    def refresh_token(self):
        data = {
            'app_id': '',
            'provider': 'password',
            'data': self._username,
            'user_info': {
                'register': False,
                'password': self._password
            }
        }
        res = requests.post('{}/auth'.format(self._url), json=data)
        if res.ok:
            json_data = res.json()
            self._token = json_data['refresh_token']['token']
            self._expires = None
            self._expired = False
            self._save_token()
            return self._token
        return None

    def _save_token(self):
        with open(self._filename, 'w') as f:
            f.write(json.dumps({'token': self._token, 'expires': self._expires}))

    def get_client(self):
        token = self.refresh_token()
        if token:
            client = GraphQLClient('{}/graphql/{}'.format(self._url, self._path))
            client.inject_token(token)
            return client
        return None





def createCard(code, zone):
        zonee = 4
        if zone == 'ESTE':
            zonee = 3

            
        obj = {
                "uuid": "1",
                "app_id": {"uuid": "1"},
                //"code": code,
                "status": False,
                "zone": {"uuid": zonee}
            }
          
        
        #estructura de un objeto usuario 
        # Agrega el array 
        

        mutation = """
            mutation CreateCard($input: CardInput) {
            createCard(input: $input, updatePolicy: ALL) {
                uuid
            }
            }
            """
        try:
            response = client.execute(mutation,variables={'input': obj})
            return response
        except Exception as e:
            return e
        
t_obj = RealmToken('https://demobsc.us1a.cloud.realm.io', '/DemoNFC4', 'realm-token.json',
                   'admindemobsc', 'V4zPU8FjL6kAf_X')
client = t_obj.get_client()





# Ejemplo
# Enviar el id del certificado y el nuevo estado
msg = createCard("")
print(msg)



