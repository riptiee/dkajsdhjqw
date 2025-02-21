#Simular 10 tiradas de dos dados. Para eso es necesario generar dos números aleatorios del 1 al 6 (inclusive) y repetir eso diez veces.
# Contar la cantidad de veces que el par de dados suma 7. Ejemplo: Si en una tirada sale un 1 y un 6 entonces suma 7 y hay que contarla, si salen un 3 y un 5, entonces no suma 7 y no se cuenta
import random
contador_de_dado7 = 0

for _ in range(10):
    dado1 = random.randint(1,6)
    dado2 = random.randint(1,6)
    dado3 = dado1 + dado2
    print("------------------------------------")
    print(f"dado 1: {dado1}")
    print(f"dado 2: {dado2}")
    print(f"la suma de estos dados da: {dado3}")
    if dado3 == 7:
     contador_de_dado7 += 1
     print("felicidades dio 7")
    else:
     print("la suma de los dados no dio el numero esperado")
print("----------------------------------------------------------")
print(f"la suma de los dados dio 7 en {contador_de_dado7} tiradas")