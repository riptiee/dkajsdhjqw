#Ejercicio. Bart Simpson quiere ahorrarse el trabajo de tener que llenar el pizarrón con una misma frase escrita muchas veces.
#Hacer un programa donde se pueda ingresar cualquier frase,
#luego se indique cuántas veces deberá repetirse, y finalmente se use un procedimiento para imprimir esa frase tantas veces como se haya pedido.

frase = input("ingresa que frase queres repetir barsinso: ")
repeticiones = int(input("¿cuantas veces lo queres repetir barsinso?: "))

for i in range(repeticiones):
        print(frase)