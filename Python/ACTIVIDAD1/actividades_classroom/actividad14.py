#Pedir 5 números y calcular el promedio. Ayuda para calcular el promedio lo que se acumula es la suma. La división se hace al final, después de terminar el for.
numeros = []
suma = 0

for n in range(5):
  numero = int(input("Decime un numero: "))
  numeros.append(numero)
  
suma_total = 0

for numero in numeros:
    suma_total += numero

promedio = suma_total / len(numeros)

print(f"El promedio de los números ingresados es: {promedio}")