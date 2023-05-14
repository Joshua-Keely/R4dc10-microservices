import requests
import pprint
import json

payload = {'some': 'data'}
chaine = json.dumps(payload)
r = requests.get('http://httpbin.org/get', data=chaine, headers={'Content-Type': 'application/json'})
print("Code de retour: ", r.status_code)
print("Headers: ")
pprint.pprint(r.headers)
contenu = r.json()
print("Contenu: ")
pprint.pprint(contenu)