import requests


url = 'http://localhost:3000/usuarios'

def get_usuario(documento):
    r = requests.get(url+'/'+str(documento))
    return r.json()

def registrar_usuario(documento, nombre):
    r = requests.post(url, json={'id': int(documento), 'nombre': nombre})
    return r.json()
# r = requests.get(url).json()

# nombre = [ n for n in r if n['nombre'].startswith('J')]