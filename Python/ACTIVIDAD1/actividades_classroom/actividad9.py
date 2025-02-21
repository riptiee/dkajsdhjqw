# Pedir 5 temperaturas al usuario y contar cuantas estan entre 10 y 30 inclusive. 
temperatura_apta = 0

for t in range(5):
    temperatura = int(input("escribe las temperaturas aqui porfavor: "))
    if temperatura >=10 and temperatura <=30:
        temperatura_apta += 1
        print(f"la temperaturas que se ha ingresado es apta")
    else:
        print(f"la temperatura que se ha ingresado no es apta")

print(f"se han ingresado {temperatura_apta} temperaturas aptas")
    

    

  