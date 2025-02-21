palabra = input("Ingresá una palabra: ")
vocales = "áéíóúüÁÉÍÓÚÜ"


cantidadDeVocalesConTilde = 0


for letra in palabra:
 if letra in vocales:
    cantidadDeVocalesConTilde = cantidadDeVocalesConTilde + 1


print(f"En '{palabra}' hay {cantidadDeVocalesConTilde} vocales con tilde")