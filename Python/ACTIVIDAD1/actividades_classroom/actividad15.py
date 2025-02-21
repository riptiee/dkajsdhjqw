#Pedir una palabra al usuario y decir que mayúsculas tiene (incluir repetidas).
#Ayuda en este caso el acumulador puede ser de tipo string o de tipo lista. Para cada caso el valor inicial y la forma de acumular son diferentes

palabra = input("ingrese una palabra. ")
letras_mayusculas = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
contador_mayusculas = 0
mayusculas = []

for letra in palabra:
    if letra in letras_mayusculas:
        contador_mayusculas += 1
        mayusculas.append(letra)
        
print(f"en {palabra} hay {contador_mayusculas} letras mayusculas")
print(f"las letras mayusculas son {mayusculas}")
