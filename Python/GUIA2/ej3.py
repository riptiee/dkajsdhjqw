#Realizar un programa que permita ingresar palabras hasta que una de
#ellas sea igual a FIN. Mostrar la palabra más larga ingresada.

def palabra_mas_larga(palabras):
    palabra_mas_larga = ""
    longitud_mas_larga = 0
    for palabra in palabras:
        longitud_actual = len(palabra)
        if longitud_actual > longitud_mas_larga:
            palabra_mas_larga = palabra
            longitud_mas_larga = longitud_actual
    return palabra_mas_larga

palabras_ = []
palabras = int(input("ingrese el maximo de palabras que va a usar: "))
for _ in range(palabras):
    palabra = input("ingrese las palabras: ")
    palabras_.append(palabra)
    if palabra == "fin" or palabra == "Fin" or palabra == "FIN" or palabra == "FiN" or palabra == "fiN" or palabra == "fIn":
      break
    concatenado = "".join(palabras_)
    if len(palabras_) > palabras:
      break
  
palabra_mas_larga = palabra_mas_larga(palabras_)
print(concatenado)
print("La palabra más larga es:", palabra_mas_larga)
