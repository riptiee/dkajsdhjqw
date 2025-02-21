#4:Realizar una función de validación para el ejercicio 2. La misma debe
#validar que los números ingresados sean correctos. La regla es que los mismos
#sean enteros, de dos cifras.

def cero():
  cero = 0
  numeros_promedio = []
  numeros = int(input("ingrese cuantos numeros desee: "))
  xdd = False
  for _ in range(numeros):
    numero = int(input("ingrese un numero de 2 cifras: "))
    numeros_promedio.append(numero)
    if len(str(numero)) <2 or len(str(numero)) >2:
        break
    if numero == cero:
        break
    xdd = True
  if xdd:
    print(sum(numeros_promedio) / numeros )
    
cero()