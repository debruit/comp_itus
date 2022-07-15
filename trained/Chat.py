import processing.Clean as Clean
import numpy as np
import pickle
import random
import json
from tensorflow.keras.models import load_model

words = pickle.load(open(f'words.pkl', 'rb'))
classes = pickle.load(open(f'classes.pkl', 'rb'))
model = load_model(f'model.h5')
intents = json.loads(open('./data/intents.json').read())

def bag_of_words(sentence, words):
    sentence_words = Clean.LemNormalize(sentence)
    bag = [0] * len(words)
    for s in sentence_words:
        for i, word in enumerate(words):
            if word == s:
                bag[i] = 1
    return np.array(bag)

def predecir_clase(sentence):
    p = bag_of_words(sentence, words)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.1
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]

    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({'intent': classes[r[0]], 'probability': str(r[1])})
    return return_list

def obtener_respuesta(ints, intents_json):
    try:
        tag = ints[0]['intent']
        list_of_intents = intents_json['intents']
        for i in list_of_intents:
            if i['tag']  == tag:
                result = [random.choice(i['responses']),tag]
                break
    except IndexError:
        result = "No entiendo tu pregunta, trata preguntando algo similar."
    return result

def respuesta_chatbot(pregunta):
    ints = predecir_clase(pregunta)
    res = obtener_respuesta(ints, intents)
    return res