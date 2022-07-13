import servicios
import secrets
import string
from datetime import datetime

token = secrets.token_urlsafe(16)

if __name__ == '__main__':
    flag = True
    saludo = 'Hola! Soy tu asistente personal. Para continuar, indícame tu número de documento. Para terminar escribe "salir"'
    saludo_personalizado = ''
    if datetime.now().hour < 12 and datetime.now().hour > 5:
        saludo_personalizado = 'Buenos días '
    elif datetime.now().hour < 18 and datetime.now().hour >= 12:
        saludo_personalizado = 'Buenas tardes '
    else:
        saludo_personalizado = 'Buenas noches '
        
    while flag:
        print(token)
        print(saludo)
        documento = input()
        if documento.lower() == 'salir':
            flag = False
            break
        usuario = servicios.get_usuario(documento)
        if usuario:
            mensaje = saludo_personalizado + usuario['nombre'] + '. Cuéntame en qué puedo ayudarte. Para terminar escribe "salir"'
            print(mensaje)
            pregunta = input()
            if pregunta.lower() == 'salir':
                flag = False
                break
            
        else:
            mensaje = 'No he podido encontrar tu usuario. Para brindarte una mejor ayuda voy a registrarte. \nIndícame tu numero de documento (sin puntos ni espacios) y tu nombre separados por una coma. \
                Ej: 123456789, Juan Pérez. \nPara terminar escribe "salir"'
            print(mensaje)
            datos = input()
            if datos.lower() == 'salir':
                flag = False
                break
            doc, nombre = datos.split(',')
            registro = servicios.registrar_usuario(doc, nombre)
            if registro:
                ok = 'Registro exitoso.'
                print(ok)   
                mensaje = saludo_personalizado + nombre + '. Cuéntame en qué puedo ayudarte. Para terminar escribe "salir"'
                print(mensaje)
                pregunta = input()
                if pregunta.lower() == 'salir':
                    flag = False
                    break
    
    print()
