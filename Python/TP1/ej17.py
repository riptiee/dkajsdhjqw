
def programita():
    tilde = "áéíóúüÁÉÍÓÚÜ"
    consonantes = "bcdfghjklmnñpqrstvwxyzBCDFGHJKLMNÑPQRSTVXYZ"
    minusculas = "abcdefghijklmnñopqrstuvwxyz"
    ptilde = 0
    pconsonantes = []
    pminusculas = []

    palabra = input("ingrese alguna palabra: ")

    for letra in palabra:
        if letra in tilde:
         ptilde = ptilde + 1
        if letra in consonantes:
         pconsonantes.append(letra)
        if letra in minusculas:
         pminusculas.append(letra)
    print(f"la palabra ingresada: {palabra} contiene {ptilde} tildes y contiene las letras consonantes: {pconsonantes} y las minusculas: {pminusculas}")
        

programita()

