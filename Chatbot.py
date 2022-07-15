import services.Servicios as Servicios
import trained.Chat as Chat
import secrets
from datetime import datetime

token = secrets.token_urlsafe(16)
texto_archivo = ''

def sal_personalizado():
    saludo_personalizado = ''
    if datetime.now().hour < 12 and datetime.now().hour > 5:
        saludo_personalizado = 'Buenos días '
    elif datetime.now().hour < 18 and datetime.now().hour >= 12:
        saludo_personalizado = 'Buenas tardes '
    else:
        saludo_personalizado = 'Buenas noches '
    return saludo_personalizado

def validacion_doc(documento):
    global texto_archivo
    while not documento.isdigit():
        documento = input('Ingrese un número de documento válido\n')
        texto_archivo += str('\nBot: Ingrese un número de documento válido')
        texto_archivo += str('\nUsuario: ' + documento)
    return documento


if __name__ == '__main__':
    texto_archivo += str('ID sesión: ' + token +
                         '\nFecha: ' + str(datetime.now()))
    flag = True
    saludo = 'Hola! Soy tu asistente personal. Para continuar, indícame tu número de documento (sin puntos ni espacios). Para terminar escribe "salir"'
    texto_archivo += str('\nBot: '+saludo)
    saludo_personalizado = sal_personalizado()

    print(saludo)
    documento = input()
    texto_archivo += str('\nUsuario: ' + documento)
    if documento.lower() == 'salir':
        flag = False
        exit()
    documento = validacion_doc(documento)
    usuario = Servicios.get_usuario(documento)
    if usuario:
        mensaje = saludo_personalizado + \
                usuario['nombre'].lstrip() + \
                '. Cuéntame en qué puedo ayudarte. Para terminar escribe "salir"'
        texto_archivo += str('\nBot: '+mensaje)
        print(mensaje)
        while flag:
            pregunta = input()
            texto_archivo += str('\nUsuario: '+pregunta)
            if pregunta.lower() == 'salir':
                flag = False
                with open('chat_'+str(usuario['id'])+'.txt', 'w') as f:
                    f.write(texto_archivo)
                exit()
            bot_respuesta = Chat.respuesta_chatbot(pregunta)
            print(bot_respuesta[0])
            texto_archivo += str('\nBot: '+bot_respuesta[0])
            if bot_respuesta[1] == 'despedidas':
                with open('chat_'+str(usuario['id'])+'.txt', 'w') as f:
                    f.write(texto_archivo)
                exit()
            

    else:
        mensaje = 'No he podido encontrar tu usuario. Para brindarte una mejor ayuda debo registrarte. ' + \
                '\nIndícame tu numero de documento (sin puntos ni espacios) y tu nombre separados por una coma. ' + \
                'Ej: 123456789, Juan Pérez. \nPara terminar escribe "salir"'
        print(mensaje)
        texto_archivo += str('\nBot: '+mensaje)
        datos = input()
        texto_archivo += str('\nUsuario: '+datos)
        if datos.lower() == 'salir':
            flag = False
            exit()
        doc, nombre = datos.split(',')
        doc = validacion_doc(doc)
        registro = Servicios.registrar_usuario(doc, nombre)
        if registro:
            ok = 'Registro exitoso.'
            texto_archivo += str('\nBot: '+ok)
            print(ok)
            mensaje = saludo_personalizado + nombre.lstrip() + \
                    '. Cuéntame en qué puedo ayudarte. Para terminar escribe "salir"'
            texto_archivo += str('\nBot: '+mensaje)
            print(mensaje)
            while flag:
                pregunta = input()
                texto_archivo += str('\nUsuario: '+pregunta)
                if pregunta.lower() == 'salir':
                    flag = False
                    with open('chat_'+doc+'.txt', 'w') as f:
                        f.write(texto_archivo)
                    exit()
                bot_respuesta = Chat.respuesta_chatbot(pregunta)
                print(bot_respuesta[0])
                texto_archivo += str('\nBot: '+bot_respuesta[0])
                if bot_respuesta[1] == 'despedidas':
                    with open('chat_'+str(usuario['id'])+'.txt', 'w') as f:
                        f.write(texto_archivo)
                    exit()
