def validar_parrafo(p):

    if not p.replace(" ", "").isalpha():
        return False
    if len(p) < 10 or len(p) > 30:
        return False
    return True

def letra_mas_repetida(p):
    frecuencia_letras = {}
    for letra in p:
        if letra != " ":
            if letra in frecuencia_letras:
                frecuencia_letras[letra] += 1
            else:
                frecuencia_letras[letra] = 1

    letra_mas_repetida = max(frecuencia_letras, key=frecuencia_letras.get)
    return letra_mas_repetida

def main():
    parrafo = input("Ingrese un párrafo de entre 10 y 30 caracteres alfabéticos o espacios: ")
    if validar_parrafo(parrafo):
        letra_repetida = letra_mas_repetida(parrafo)
        print(f"La letra más repetida en el párrafo es: {letra_repetida}")
    else:
        print("El párrafo ingresado no cumple con los requisitos.")

if __name__ == "__main__":
    main()