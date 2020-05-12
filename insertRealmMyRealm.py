# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import pandas as pd
import json
# from pandas import json
from datetime import datetime
from graphqlclient import GraphQLClient
import requests
import os.path
import uuid
import csv

urlRealm = 'https://demobsc.us1a.cloud.realm.io'
MyRealm = 'bd204e2c5813ea61007af86b16c7a449/myRealm'
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

def mutationActionsMenu(actionsmenu):
    # print(app)
    mutation = """
    mutation CreateActionsMenus($input: [ActionsMenuInput!]) {
      createActionsMenus(input: $input, updatePolicy: ALL) {
        uuid
      }
    }
    """
    response = client.execute(mutation,variables={'input': actionsmenu})
    return response

def mutationTypeContent(typecontent):
    print(app)
    mutation = """
    mutation CreateTypeContent($input: TypeContentInput!) {
      createTypeContent(input: $input, updatePolicy: ALL) {
        uuid
      }
    }
    """
    response = client.execute(mutation,variables={'input': typecontent})
    return response

def mutationMenu(menu):
    mutation = """
    mutation CreateMenu($input: MenuInput!) {
      createMenu(input: $input, updatePolicy: ALL) {
        uuid
      }
    }
    """
    response = client.execute(mutation,variables={'input': menu})
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

def mutationContent(contents):
    # print(translates)
    mutation = """
    mutation CreateContents($input: [ContentInput!]) {
      createContents(input: $input, updatePolicy: ALL) {
        uuid
      }
    }
    """
    response = client.execute(mutation,variables={'input': contents})
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
    "name": 'BSC'
        }

actionsmenu = [
    {
      "uuid": "1a3e79af-22ae-44a3-a2d8-0b61a6d0d314",
      "name": "Home",
      "icon": "home",
      "sections": [
       {
      "uuid": "4c992b5f-5bdd-45ed-a3c4-bb7c7d4ff181",
      "sequence": 1,
      "limit": 3,
      "name": "Pròximos eventos"
    },
    {
      "uuid": "a20166ca-300f-4e5b-ab3c-c27178999155",
      "sequence": 3,
      "limit": 4,
      "name": "Màs comprados"
    },
    {
      "uuid": "9f68653a-0451-4255-b68d-804653283112",
      "sequence": 2,
      "limit": 3,
      "name": "Mas buscados"
    },
    {
      "uuid": "a85b07a2-67b4-4985-bb14-1dc957b499ed",
      "sequence": 4,
      "limit": 2,
      "name": "Tendencias"
    }
      ],
      "icon_type": "fontisto"
    },
    {
      "uuid": "f458b6f5-e298-41ea-93df-fb246915c2c7",
      "name": "Tickets",
      "icon": "ticket",
      "sections": [],
      "icon_type": "entypo"
    },
    {
      "uuid": "707e2ca8-7326-4345-adfe-b93bab14e2b2",
      "name": "Search",
      "icon": "search",
      "sections": [],
      "icon_type": "fontisto"
    },
    {
      "uuid": "97ff03c3-039d-4863-bcdd-f40a0b22bc67",
      "name": "Menu",
      "icon": "menu",
      "sections": [],
      "icon_type": "material-icons"
    },
    {
      "uuid": "4a5d0a69-64b1-4440-b536-dbb57544424b",
      "name": "Wish",
      "icon": "heart",
      "sections": [],
      "icon_type": "material-community"
    }
  ]

typecontent = {
      "uuid": "769acbd6-3791-4206-bc85-c5d674d8f991",
      "app": {"uuid": "1"},
      "name": "Tickets",
      "action": {"uuid": "ca7259e5-986b-45be-8524-88e26d170592"}
    #   "isItemMenu": 
    }



menu = {
      "uuid": "55f66633-5cae-4450-9ac4-5c0be4329c7c",
      "app": {"uuid": "1"},
      "actionsMenu": [
        {"uuid": "1a3e79af-22ae-44a3-a2d8-0b61a6d0d314"},
        {"uuid": "f458b6f5-e298-41ea-93df-fb246915c2c7"},
        {"uuid": "707e2ca8-7326-4345-adfe-b93bab14e2b2"},
        {"uuid": "97ff03c3-039d-4863-bcdd-f40a0b22bc67"},
        {"uuid": "4a5d0a69-64b1-4440-b536-dbb57544424b"}
      ]
    }

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

contents = [
    {
      "uuid": "4a4f5b86-79c3-4fde-a578-953486d73a93",
      "app": {"uuid": "1"},
      "typeContent": {"uuid": "769acbd6-3791-4206-bc85-c5d674d8f991"},
      "section": {"uuid": "4c992b5f-5bdd-45ed-a3c4-bb7c7d4ff181"},
      "name": "Barcelona vs Junior",
      "title": "Barcelona vs Junior",
      "subtitle": "Fase de Grupos Copa Libertadores",
      "date": "2020-12-01T05:00:00.000Z",
      "image": "https://depor.com/resizer/GVvRS8L0Tm75XnkhR9vRUujIwSQ=/980x528/smart/arc-anglerfish-arc2-prod-elcomercio.s3.amazonaws.com/public/I2V3N7CDXRA6JM63ZKBVSMVGBA.jpg",
      "summary": "Estadio Monumental Isidro Romero Carbo",
    #   "create_at": null,
    #   "date_expire": null
    },
    {
      "uuid": "83b55f8c-0964-4f1a-8455-3894ef6cb893",
      "app": {"uuid": "1"},
      "typeContent": {"uuid": "769acbd6-3791-4206-bc85-c5d674d8f991"},
      "section": {"uuid": "a20166ca-300f-4e5b-ab3c-c27178999155"},
      "name": "Barcelona vs Junior",
      "title": "Barcelona vs Junior",
      "subtitle": "Fase de Grupos Copa Libertadores",
      "date": "2020-12-01T05:00:00.000Z",
      "image": "https://hinchaamarillo.com/wp-content/uploads/2019/05/bsc-vs-cdo.jpg",
      "summary": "Estadio Monumental Isidro Romero Carbo",
    #   "create_at": null,
    #   "date_expire": null
    },
    {
      "uuid": "68ab128a-ee51-41db-b1fe-fa658a66be2c",
      "app": {"uuid": "1"},
      "typeContent": {"uuid": "769acbd6-3791-4206-bc85-c5d674d8f991"},
      "section": {"uuid": "9f68653a-0451-4255-b68d-804653283112"},
      "name": "Barcelona vs Junior",
      "title": "Barcelona vs Junior",
      "subtitle": "Fase de Grupos Copa Libertadores",
      "date": "2020-12-01T05:00:00.000Z",
      "image": "https://depor.com/resizer/GVvRS8L0Tm75XnkhR9vRUujIwSQ=/980x528/smart/arc-anglerfish-arc2-prod-elcomercio.s3.amazonaws.com/public/I2V3N7CDXRA6JM63ZKBVSMVGBA.jpg",
      "summary": "Estadio Monumental Isidro Romero Carbo",
    #   "create_at": null,
    #   "date_expire": null
    },
    {
      "uuid": "1a573f06-d0f6-4cca-9801-69a0a3dc65c7",
      "app": {"uuid": "1"},
      "typeContent": {"uuid": "769acbd6-3791-4206-bc85-c5d674d8f991"},
      "section": {"uuid": "9f68653a-0451-4255-b68d-804653283112"},
      "name": "Barcelona vs Junior",
      "title": "Barcelona vs Junior",
      "subtitle": "Fase de Grupos Copa Libertadores",
      "date": "2020-12-01T05:00:00.000Z",
      "image": "https://hinchaamarillo.com/wp-content/uploads/2019/05/bsc-vs-cdo.jpg",
      "summary": "Estadio Monumental Isidro Romero Carbo",
    #   "create_at": null,
    #   "date_expire": null
    },
    {
      "uuid": "47f5ffa3-b51f-4548-9878-c5a3c1aff2a2",
      "app": {"uuid": "1"},
      "typeContent": {"uuid": "769acbd6-3791-4206-bc85-c5d674d8f991"},
      "section": {"uuid": "9f68653a-0451-4255-b68d-804653283112"},
      "name": "Barcelona vs Junior",
      "title": "Barcelona vs Junior",
      "subtitle": "Fase de Grupos Copa Libertadores",
      "date": "2020-12-01T05:00:00.000Z",
      "image": "https://hinchaamarillo.com/wp-content/uploads/2019/05/bsc-vs-cdo.jpg",
      "summary": "Estadio Monumental Isidro Romero Carbo",
    #   "create_at": null,
    #   "date_expire": null
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
    







# resp = mutationApp(app)
# print(resp)

# resp = mutationActionsMenu(actionsmenu)
# print(resp)

# resp = mutationMenu(menu)
# print(resp)

# resp = mutationTypeContent(typecontent)
# print(resp)

resp = mutationContent(contents)
print(resp)


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

# resp = mutationUsers(users)
# print(resp)