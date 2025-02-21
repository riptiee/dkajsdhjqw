numeros = []

for n in range(5):
    numero = int(input("Ingrese un número: "))
    numeros.append(numero)
  
numeros_pares = 0
for numero in numeros:
    if numero % 2 == 0:
        numeros_pares += 1
        
print(f"En '{numeros}' hay {numeros_pares} numeros pares")
  
  
  

