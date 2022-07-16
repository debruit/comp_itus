CHATBOT V1


Esta es una primera versión del chatbot itus. 

El chatbot utiliza una base de conocimiento predeterminada para responder preguntas generales y específicas de los usuarios. Esta base de conocimiento hace que el chatbot sea de tipo basado en reglas donde utiliza una red neuronal para clasificar las preguntas de los usuarios en las posibles clases que se encuentran en la base del conocimiento. Asimismo, dada la clasificacion, se obtiene una respuesta de la misma base para retornar al usuario.

El proceso por el que pasa una pregunta u oracion del usuario es el siguiente: 
1. Se hace una limpieza de la pregunta u oración removiendo signos de puntuación y palabras que no son relevantes (stopwords).
2. Luego de la limpieza, el modelo de aprendizaje automático recibe la pregunta para predecir su clase en la base de conocimiento y poder retornar una respuesta adecuada.
3. La red neuronal compara, entonces, esta palabra en la base de conocimiento y retorna la respuesta de la clase con la probabilidad más alta a donde pertenece la pregunta del usuario.

Para probar la implementación del chatbot se debe seguir los siguientes pasos:
1. A traves de la linea de comando correr 'json-server --watch data/db.json' para generar la base de datos fictisia que permite los API requests que utiliza el bot para validar al usuario.
2. Correr el archivo Chatbot.py a través de la linea de comandos 'python Chatbot.py'. El bot responderá pidiendo el número de documento para validar el usuario en la bd fictisia. Si no lo encuentra le pedirá el número de documento y el nombre para registrarlo. 

Proceso de un chat con el chatbot:
1. Se genera una llave única que sirve como el ID de la sesión del chat.
2. Una vez validado el usuario el bot dará un saludo personalizado dependiendo también de la zona horaria. Desde aquí comienza la interaccion conversacional con el bot.

Una vez se despida del bot, este guardará una copia del chat en un archivo .txt que podrá ser consultado posteriormente.

################################

Para generar una nueva base de conocimiento se debe modificar el archivo data/intents.json con las nuevas reglas que usará el bot.
Luego, se debe descomentar la linea train_model() del archivo Clean.py y ejecutarlo 'python Clean.py'. Esto permitirá crear una nueva lista de palabras y clases de la base de conocimiento junto con un nuevo modelo de red neuronal para ser usado en el chatbot.