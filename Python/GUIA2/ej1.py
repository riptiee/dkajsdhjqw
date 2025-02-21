def palabra_mas_larga(palabras):
    palabra_mas_larga = ""
    longitud_mas_larga = 0
    for palabra in palabras:
        longitud_actual = len(palabra)
        if longitud_actual > longitud_mas_larga:
            palabra_mas_larga = palabra
            longitud_mas_larga = longitud_actual
    return palabra_mas_larga

palabras = []
contador = 0
while contador < 3:
    palabra = input(f"Ingrese la palabra {contador + 1}: ")
    palabras.append(palabra)
    contador += 1

palabra_mas_larga = palabra_mas_larga(palabras)

print("La palabra más larga es:", palabra_mas_larga)