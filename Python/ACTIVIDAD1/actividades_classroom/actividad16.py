
palabra = input("ingrese una palabra. ")
letras_mayusculas = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
contador_mayusculas = 0
mayusculas = []
repetidos = False

for letra in palabra:
    if letra in letras_mayusculas:
        contador_mayusculas += 1
        mayusculas.append(letra)
    if mayusculas.count (letra) > 1:
        repetidos = True

if repetidos:
    mayusculas_sin_repetir = set(mayusculas)

print(f"en {palabra} hay {contador_mayusculas} letras mayusculas")
print(f"las letras mayusculas son {mayusculas_sin_repetir}")