#Pedir un numero, tirar un dado tantas veces como digo el numero y cuenta cuantas veces sale en 6. Ejemplo si el usuario ingresa un 5 se tiran 5 dados
import random

veces = int(input("ingrese un numero: "))

numero_6 = 0

for dados in range(veces):
    dado = random.randint(1,6)
    print(f"en el dado salio: {dado}")
    if dado == 6:
        numero_6 += 1
        
print(f"el dado numero 6 ha salido {numero_6} veces")
    
    

         
    
    


    
