#2: Realizar un programa que permita ingresar números. El ingreso debe
#finalizar al cargar el valor cero. Mostrar a continuación el promedio.
def cero():
  cero = 0
  numeros_promedio = []
  numeros = int(input("ingrese cuantos numeros desee: "))
  for _ in range(numeros):
    numero = int(input("ingrese un numero: "))
    numeros_promedio.append(numero)
    if numero == cero:
        break
  print(sum(numeros_promedio) / numeros )

cero()