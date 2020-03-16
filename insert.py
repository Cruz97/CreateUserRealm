# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
# import pandas as pd
import json
from datetime import datetime
from graphqlclient import GraphQLClient
import requests
import os.path
import uuid
import csv

urlRealm = 'https://demobsc.us1a.cloud.realm.io'
MyRealm = '/DemoNFC7'
fileToken = 'realm-token.json'
userRealm = 'admindemobsc'
passRealm = 'V4zPU8FjL6kAf_X'

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

def mutationApp(newapp):
    print(app)
    mutation = """
    mutation CreateApp($input: AppInput!) {
      createApp(input: $input, updatePolicy: ALL) {
        uuid
      }
    }
    """
    response = client.execute(mutation,variables={'input': newapp})
    return response

def mutationAppConfiguration(appconfiguration):
    print(app)
    mutation = """
    mutation CreateAppConfiguration($input: AppConfigurationInput!) {
      createAppConfiguration(input: $input, updatePolicy: ALL) {
        uuid
      }
    }
    """
    response = client.execute(mutation,variables={'input': appconfiguration})
    return response

def mutationAppCustom(appcustom):
    print(app)
    mutation = """
    mutation CreateAppCustom($input: AppCustomInput!) {
      createAppCustom(input: $input, updatePolicy: ALL) {
        uuid
      }
    }
    """
    response = client.execute(mutation,variables={'input': appcustom})
    return response

def mutationLanguage(languages):
    print(languages)
    mutation = """
    mutation CreateLanguages($input: [LanguageInput!]) {
      createLanguages(input: $input, updatePolicy: ALL) {
        uuid
      }
    }
    """
    response = client.execute(mutation,variables={'input': languages})
    return response

def mutationTranslate(translates):
    # print(translates)
    mutation = """
    mutation CreateTranslates($input: [TranslateInput!]) {
      createTranslates(input: $input, updatePolicy: ALL) {
        uuid
      }
    }
    """
    response = client.execute(mutation,variables={'input': translates})
    return response

def mutationAppImages(appimages):
    # print(translates)
    mutation = """
    mutation CreateAppImages($input: [AppImageInput!]) {
      createAppImages(input: $input, updatePolicy: ALL) {
        uuid
      }
    }
    """
    response = client.execute(mutation,variables={'input': appimages})
    return response

def mutationAppContent(appcontent):
    # print(translates)
    mutation = """
    mutation CreateAppContents($input: [AppContentInput!]) {
      createAppContents(input: $input, updatePolicy: ALL) {
        uuid
      }
    }
    """
    response = client.execute(mutation,variables={'input': appcontent})
    return response

def mutationAppContentSection(appcontentsection):
    # print(translates)
    mutation = """
    mutation CreateAppContentSections($input: [AppContentSectionInput!]) {
      createAppContentSections(input: $input, updatePolicy: ALL) {
        uuid
      }
    }
    """
    response = client.execute(mutation,variables={'input': appcontentsection})
    return response
        
def mutationZone(zones):
    # print(translates)
    mutation = """
    mutation CreateZones($input: [ZoneInput!]) {
      createZones(input: $input, updatePolicy: ALL) {
        uuid
      }
    }
    """
    response = client.execute(mutation,variables={'input': zones})
    return response
        
def mutationCards(cards):
    # print(translates)
    mutation = """
    mutation CreateCards($input: [CardInput!]) {
      createCards(input: $input, updatePolicy: ALL) {
        uuid
      }
    }
    """
    response = client.execute(mutation,variables={'input': cards})
    return response

def mutationUsers(users):
    mutation = """
    mutation CreateUsers($input: [UserInput!]) {
      createUsers(input: $input, updatePolicy: ALL) {
        uuid
      }
    }
    """
    response = client.execute(mutation,variables={'input': users})
    return response
    
def mutationEvent(event):
    # print(translates)
    mutation = """
    mutation CreateEvent($input: EventInput!) {
      createEvent(input: $input, updatePolicy: ALL) {
        uuid
      }
    }
    """
    response = client.execute(mutation,variables={'input': event})
    return response

    

t_obj = RealmToken(urlRealm, MyRealm, fileToken ,userRealm, passRealm)
client = t_obj.get_client()
# print(client.token)


app = {
    "uuid": '1',
    "name": 'BSC',
    "name2": 'BSC2'
        }

appconfiguration = {
    "uuid": "1",
    "app_id": {"uuid": "1"},
    "host": 'string?',
    "port": 443,
    "database": 'string?',
    "username": 'string?', 
    "password": 'string?',
    "protocol": 'string?',
    "token": 'string?',
    "secret": 'string?'  
}

appcustom = {
    "uuid": "1",
    "app_id": {"uuid": "1"},
     "icon": 'https://3.bp.blogspot.com/-4Jq0XHT9G-g/WWADtk_BlyI/AAAAAAABMEg/q843jZLXcFQLxv0yGpmc_W3N9SBFGViSACLcBGAs/s1600/Barcelona%2BSporting%2BClub256x.png',
    # "icon_alt": 'string',
    "loading_icon": 'https://3.bp.blogspot.com/-4Jq0XHT9G-g/WWADtk_BlyI/AAAAAAABMEg/q843jZLXcFQLxv0yGpmc_W3N9SBFGViSACLcBGAs/s1600/Barcelona%2BSporting%2BClub256x.png',
    "loading_bg": '#EEC413',
    "theme_color_primary": '#FFF218',
    "theme_color_secondary": '#ff4000',
    # "theme_color_success": 'string',
    # "theme_color_info": 'string',
    # "theme_color_warning": 'string',
    # "theme_color_danger": 'string',
    # "theme_bg": 'string?',
    # "theme_bg_alt": 'string?',
    "login_bg": 'https://instagram.fvno2-1.fna.fbcdn.net/v/t51.2885-15/e35/s1080x1080/80845296_178720716867553_5572538001568266457_n.jpg?_nc_ht=instagram.fvno2-1.fna.fbcdn.net&_nc_cat=101&_nc_ohc=bhqbZPWmf2cAX_IN_R_&oh=230a8c8e1debb18e74baa59ff725c89f&oe=5ED5A90F',
    # "login_mode": 'string?',
    "theme_color_text_primary": '#FFFFFF',
    "theme_color_text_secondary": '#013978'
}


languages = [
    {
        "uuid": "1",
        "name": "Spanish",
        "language": "es"
    },
    {
        "uuid": "2",
        "name": "English",
        "language": "en"
    }
]

translates = [
    {
      "uuid": "131ac76b-e045-40ba-8a43-7cb7ceebb8a5",
      "section": "login",
      "label": "Numero_de_socio",
      "value": "Membership Number",
      "app_id": {
          "uuid": "1"
          },
      "language": {
          "uuid": "2"
      }
    },
    {
      "uuid": "b26996b7-aed5-44aa-a2fa-70abc6f220e6",
      "section": "login",
      "label": "Numero_de_socio",
      "value": "Numero de socio",
      "app_id": {
          "uuid": "1"
          },
      "language": {
          "uuid": "1"
      }
    },
    {
      "uuid": "08590f18-9557-4394-abef-9cfefe578434",
      "section": "login",
      "label": "Correo",
      "value": "Correo Electrónico ",
            "app_id": {
          "uuid": "1"
          },
      "language": {
          "uuid": "1"
      }
    },
    {
      "uuid": "06794b2f-424a-4b12-bd51-664ecf380b00",
      "section": "login",
      "label": "Correo",
      "value": "Email",
            "app_id": {
          "uuid": "1"
          },
      "language": {
          "uuid": "2"
      }
    },
    {
      "uuid": "70bd18f4-53dd-436f-8a3a-80a4082f1416",
      "section": "login",
      "label": "Generar_PIN",
      "value": "Generar PIN",
            "app_id": {
          "uuid": "1"
          },
      "language": {
          "uuid": "1"
      }
    },
    {
      "uuid": "ff99104d-ba12-49ed-81c6-1cadc22e3485",
      "section": "login",
      "label": "Generar_PIN",
      "value": "Generate PIN",
            "app_id": {
          "uuid": "1"
          },
      "language": {
          "uuid": "2"
      }
    }
  ]

images = [
    {
      "uuid": "a136d3d6-a245-408c-87b0-ccd97d3527dc",
      "app_id": {"uuid": "1"},
      "name": "FASE2_BSC",
      "url": "https://www.primicias.ec/wp-content/uploads/2020/02/Barcelona-1024x574.jpeg",
      "caption": "BSC vs SC "
    },
    {
      "uuid": "bd160d67-37f4-4aac-9fd9-28e57d71e541",
      "app_id": {"uuid": "1"},
      "name": "EntrenamientoBSCFase2",
      "url": "https://barcelonasc.com.ec/noticias/wp-content/uploads/2020/02/sCristal02.png",
      "caption": "aaa"
    }
  ]

appcontent = [
    {
        "uuid": '1',
        "app_id": {"uuid": "1"},
        "title": 'Title App Content 1',
        # "type_id": [],
        # "categories": [],
        "subtitle": 'Subtitle App Content 1',
        "date": '2020-01-01',
        "image": {
            "uuid": "1",
            "app_id": {
                "uuid": "1"
            },
            "name": "Post1",
            "url": "https://barcelonasc.com.ec/noticias/wp-content/uploads/2020/02/Web.png",
            "caption": ""
            },
        # "body": 'string?',
        "gallery": [],
        "summary": 'Summary App Content',
        # "sections": [{"uuid":"1"}]
    },
      {
        "uuid": '2',
        "app_id": {"uuid": "1"},
        "title": 'Title App Content 2',
        # "type_id": [],
        # "categories": [],
        "subtitle": 'Subtitle App Content 2',
        "date": '2020-01-01',
        "image": {
            "uuid": "2",
            "app_id": {
                "uuid": "1"
            },
            "name": "Post2",
            "url": "https://barcelonasc.com.ec/noticias/wp-content/uploads/2020/02/Practicas16.png",
            "caption": ""
            },
        # "body": 'string?',
        "gallery": [],
        "summary": 'Summary App Content',
        # "sections": [{"uuid":"1"}]
    },
      {
        "uuid": '3',
        "app_id": {"uuid": "1"},
        "title": 'Title App Content 3',
        # "type_id": [],
        # "categories": [],
        "subtitle": 'Subtitle App Content 3',
        "date": '2020-01-01',
        "image": {
            "uuid": "3",
            "app_id": {
                "uuid": "1"
            },
            "name": "Post3",
            "url": "https://barcelonasc.com.ec/noticias/wp-content/uploads/2020/02/sCristal05.png",
            "caption": ""
            },
        # "body": 'string?',
        "gallery": [],
        "summary": 'Summary App Content',
        # "sections": [{"uuid":"1"}]
    }
]

appcontentsection = [
    {
        "uuid": "1",
        "name": "Ultimas noticias",
        "app_id": {"uuid": "1"},
        "items": [
            {
            "uuid": '1',
            "app_id": {"uuid": "1"},
            "content_id" : {"uuid": "1"},
            "sequence": 1
            },
             {
            "uuid": '2',
            "app_id": {"uuid": "1"},
            "content_id" : {"uuid": "2"},
            "sequence": 2
            }
           
            
        ]
    },
     {
        "uuid": "2",
        "name": "Proximos Partidos",
        "app_id": {"uuid": "1"},
        # type: 'string?',
        # icon: 'string?',
        "items": [
               {
                "uuid": '3',
                "app_id": {"uuid": "1"},
                "content_id" : {"uuid": "3"},
                "sequence": 1
            }
        ]
    }
]

appzones = [
    {
    "uuid": "1",
    "name": "ESTE"
    },
    {
    "uuid": "2",
    "name": "OESTE"
    }
]

cards = [
    {
        "uuid": str(uuid.uuid1()),
        "app_id": {"uuid":"1"},
        "code": "953161800",
        "status": False,
        "zone": {"uuid": "1"},
        "type": "NFC"
    },
    {
        "uuid": str(uuid.uuid1()),
        "app_id": {"uuid":"1"},
        "code": "954111592",
        "status": False,
        "zone": {"uuid": "1"},
         "type": "NFC"
    },
    {
        "uuid": str(uuid.uuid1()),
        "app_id": {"uuid":"1"},
        "code": "955231064",
        "status": False,
        "zone": {"uuid": "2"},
        "type": "NFC"
    },
    {
        "uuid": str(uuid.uuid1()),
        "app_id": {"uuid":"1"},
        "code": "700146421",
        "status": False,
        "zone": {"uuid": "2"},
         "type": "NFC"
    }
]

users = [
    {
        # "uuid": str(uuid.uuid1()),
        "uuid": "23a06926-531d-11ea-8eb1-3c15c2e0c3d2",
        "app_id": {"uuid": "1"},
        "name": "USER 1",
        "code": "111",
        "zone": {"uuid": "1"},
        "event": {"uuid":"3"},
        "create_at": str(datetime.now())
    },
    {
        # "uuid": str(uuid.uuid1()),
         "uuid": "23a06a51-531d-11ea-8c99-3c15c2e0c3d2",
        "app_id": {"uuid": "1"},
        "name": "USER 2",
        "code": "222",
        "zone": {"uuid": "1"},
        "event": {"uuid":"3"},
        "create_at": str(datetime.now())
    },
    {
        # "uuid": str(uuid.uuid1()),
         "uuid": "23a06af3-531d-11ea-90bd-3c15c2e0c3d2",
        "app_id": {"uuid": "1"},
        "name": "USER 3",
        "code": "333",
        "zone": {"uuid": "2"},
        "event": {"uuid":"3"},
        "create_at": str(datetime.now())
    },
    {
        # "uuid": str(uuid.uuid1()),
         "uuid": "23a06b7d-531d-11ea-8635-3c15c2e0c3d2",
        "app_id": {"uuid": "1"},
        "name": "USER 4",
        "code": "444",
        "zone": {"uuid": "2"},
        "event": {"uuid":"3"},
        "create_at": str(datetime.now())
    }
]

# event = {
#     "uuid": "1",
#     "name": "Partido Copa libertadores Fase 3 Barcelona vs Cerro Porteno",
#     "title": "Barcelona vs Cerro Porteno",
#     "subtitle": "Copa libertadores Fase 3",
#     "date": str(datetime.now()),
#     "image": {
#         "uuid": str(uuid.uuid1()),
#         "app_id": {"uuid": "1"},
#         "name": "Libertadores Fase 3",
#         "url": "",
#         "caption": "caption1"
#     },
#     "summary": "",
#     "app_id": {"uuid": "1"},
#     "created_at": str(datetime.now()),
#     "date_expire": (str(datetime.now()))
# }



# resp = mutationApp(app)
# print(resp)
# resp = mutationEvent(event)
# print(resp)
# resp = mutationZone(appzones)
# print(resp)
# resp = mutationUsers(users)
# print(resp)

# with open('codigos2.csv') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=';')
#     line_count = 0
#     list_arrays = []
#     array_cards = []
#     for row in csv_reader:
#         if line_count == 0:
#             line_count += 1
#         else:
#             zone = 1
#             if str(row[0])== 'OESTE' :
#                 zone = 2
#             card = {
#                 "uuid": str(uuid.uuid1()),
#                 "app_id": {"uuid":"1"},
#                 "code": str(row[1]),
#                 "qr": str(row[2]),
#                 "status": False,
#                 "zone": {"uuid": str(zone)},
#                 "type": "NFC"
#             }
#             array_cards.append(card)
#             line_count += 1

#     print(len(array_cards))
#     lote = 100
#     iteraciones = len(array_cards) / 100
#     faltantes = len(array_cards) % 100
#     ini = 0
#     fin = 0
#     for i in range(0,iteraciones+1):
#         fin = ini + (lote)
        
#         resp = mutationCards(array_cards[ini:fin])
#         print(resp)
#         # print(str(ini) + ' => ' +str(fin))
#         ini = (fin)

#     # print(str(ini) + ' => ' +str(len(array_cards)))
#     resp2 = mutationCards(array_cards[ini: len(array_cards)])
#     print(resp2)
    







# resp = mutationAppConfiguration(appconfiguration)
# print(resp)
# resp = mutationAppCustom(appcustom)
# resp = mutationLanguage(languages)
# print(resp)
# resp = mutationTranslate(translates)
# print(resp)
# resp = mutationAppContent(appcontent)
# print(resp)
# # resp = mutationAppContentSection(appcontentsection)
# # print(resp)
# resp = mutationZone(appzones)
# print(resp)
# resp = mutationCards(cards)
# print(resp)

resp = mutationUsers(users)
print(resp)