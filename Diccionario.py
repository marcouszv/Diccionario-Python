import time
meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "ROFL": "Una respuesta a una broma",
            "SHEESH": "Ligera desaprobación",
            "CREEPY": "Aterrador, Siniestro",
            "AGGRO": "Ponerse agresivo/enojado"
            }
            

for _ in meme_dict:
    print("Hola, este proyecto es un diccionario para ayudar a entender las palabras modernas")
    time.sleep(1)
    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("La palabra no se encuentra en el diccionario")

print("Gracias por usar el diccionario")

#Marcouszv$
