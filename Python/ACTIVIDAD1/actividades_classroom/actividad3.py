def pide_numeros():
  numeros=[]
  n = int(input("¿Cuantos numeros quieres ingresar? "))
  for i in range(n):
    num = int(input(f"Ingresar numero {i+1}: "))
    numeros.append(num)
  return numeros

def detectar_negativo(numeros):
  for num in numeros:
    if num < 0:
      return True


numeros = pide_numeros()
negativo = detectar_negativo(numeros)

if negativo:
  print("se detecto numeros negativos")
else:
  print("no se detecto numeros negativos")