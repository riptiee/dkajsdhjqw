#Ejercicio Calcular el producto (multiplicación) de los números del 1 al 100 que sean múltiplos de 2 o de 5.
#Cuidado: ¿Cuál debería ser el valor inicial del acumulador si la operación que vamos a hacer es una multiplicación?

def calcular_producto():
    
    lista_numeros = []
    for numero in range(1, 100):
        lista_numeros.append(numero)   
    lista_nueva = [lista_numeros[0]]
    for numeros in range(len(lista_numeros)):
        if numeros %2 == 0 or numeros %5 == 0:
            numeroM = numero * lista_nueva(-1)
            lista_nueva.append(numeroM)
            
    print(f"""lista de numeros multiplicados del 1 al 100: 
          {lista_nueva}""")
            
def main():

    calcular_producto()
    
if __name__ == "__main__":
    main()
    