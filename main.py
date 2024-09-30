meme_dict = {
    "CRINGE": "Algo excepcionalmente raro",
    "LOL": "Una respuesta común a algo gracioso",
    "OHIO": "Ciudad en estados unidos🦅🦅🦅",
}
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

if word in meme_dict.keys():
    print(word,meme_dict[word])
else:
    print
