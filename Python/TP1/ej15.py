def contador_palabras(texto):
    palabras = texto.split()
    return len(palabras)

palabra = input("ingrese muchas palabras ")
blabla = contador_palabras(palabra)
print(f"El numero de palabras en el texto es: {blabla}" )