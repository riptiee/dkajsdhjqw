#Generar 10 numeros al azar entre 1 y 10 y contar cuantos son mayores a 5.
import random

print("generar 10 numeros al azar:")
print("----------------------------")
for numero in range(10):
    numero = random.randint(1,10)
    print(f"te toco el numero {numero}")
    if (numero>5):
     print("este numero es mayor a 5")
    else:
     print("este numero no es mayor a 5")


 



        
