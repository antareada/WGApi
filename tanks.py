import requests
import json

s = requests.Session()
application_id = '01832d316a2655bc17523d78862950fc'

r = s.get("https://api.worldoftanks.ru/wot/encyclopedia/tanks/?application_id=demo&fields=name,type,level").json()
f = open('tanks.txt', 'w')
json.dump(r, f, indent=2)