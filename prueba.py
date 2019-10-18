from langdetect import detect

sentences = ["hello, how are you",
             "Hola cómo estás",
             "x3ads"]



oracion = "Si puede, evite pasar por el"
for item in oracion.split():
    print(item)
    print(detect(item))