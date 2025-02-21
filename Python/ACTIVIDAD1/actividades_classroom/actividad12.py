#Ejercicio Probar el código de ejemplo que suma todos los números desde 1 hasta el indicado por el usuario. Luego modificarlo para que sume sólamente los números impares.

maximo = int(input("Decime un número: "))
suma = 0
numeros_impares = 0

for i in range(1, maximo+1):
    if i %2 != 0: 
        suma += i
        numeros_impares += 1

print(f"la suma de los numeros del 1 al {maximo} es {suma} y sumando solo {numeros_impares} impares")

        
