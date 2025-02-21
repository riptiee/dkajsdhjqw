#1
#A:
lista_numeros = []
numeros = int(input("A ingrese cuantos numeros va a ingresar: "))
for _ in range(numeros):
  numero = int(input("A ingrese un numero: "))
  if numero != 0:
   lista_numeros.append(numero)
  else:
      break
#B
numero = int(input("B ingrese un numero para eliminar: "))
if numero in lista_numeros:
  lista_numeros.remove(numero)
else:
  print("B ese numero no se encuentra en la lista")
#C
print(f"la suma de los numeros es: {sum(lista_numeros)}")
#D
numero = int(input("D ingrese que parte de la lista quiere: "))
print(lista_numeros[ : numero])
#E
nueva_lista = set()
for numero in lista_numeros:
  cantidad = lista_numeros.count(numero)
  nueva_lista.add((numero , cantidad))

print(nueva_lista)