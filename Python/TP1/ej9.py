#Ejercicio. Escribir un programa que le pida al usuario una cantidad de dados y luego arroje tantos dados al azar como se le indicó.
#La parte del programa que elige los números al azar y los muestra debe ser un procedimiento.
import random
tiradas = int(input("¿cuantas dados queres tirar?: "))

for i in range(tiradas):
    dado = random.randint (1,6)
    print(dado)