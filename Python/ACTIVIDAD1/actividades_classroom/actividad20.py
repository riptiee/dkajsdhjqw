import random

cuantosPositivos = 0
cuantosNegativos = 0
total = 0
salioUnCero = False

for _ in range(10):  
  numero = random.randint(-5, 6)
  print(numero)

  if numero == 0:
    salioUnCero = True
  if numero < 0:
    numero = 0
    cuantosNegativos = cuantosNegativos + 1
  if numero > 0:
    cuantosPositivos = cuantosPositivos + 1
    total = total + numero
  
print()
print(f"La suma de todos los números positivos dio {total}")
print(f"Hubo {cuantosNegativos} números negativos")
if salioUnCero:
  print("Salió al menos un cero")
else:
  print("No salió ningún cero")