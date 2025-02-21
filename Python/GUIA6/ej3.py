#Ejercicio 3: Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla,
#pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta.
#Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.

def verduleria():
    
    frutas = {
        'banana' : 150,
        'manzana': 98, 
        'pera' : 120,
        'naranja' : 100,
    }
        
    pregunta = input("que fruta desea comprar? ").lower()
    precio = int(input("cuantos kilos desea llevar? "))
    
    if pregunta in frutas:
        print(f"El total de {pregunta} es: {frutas[pregunta] * precio}.")
    else:
        print("No vendemos esa fruta.")
        
def main():
    verduleria()
    
if __name__ == "__main__":
    main()