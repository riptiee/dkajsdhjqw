import random

def lista_palabras_1(listado_palabras):
    
    print("Lista 1:") 
    while True:
        palabras = input("Ingrese una palabra (o 'fin' para terminar): ")
        if palabras.lower() == 'fin':
            break
        listado_palabras.append(palabras)
    return listado_palabras

def repetidos(listado_palabras):
    
    repetido = False
    for palabras in listado_palabras:
        palabra_rep = listado_palabras.count(palabras)
        if palabra_rep >1:
            repetido = True
    print(repetido)

def numeros_aleatorios(repetidos):
    
    lista_numeros = []
    for _ in range(23):
        numero = random.randint(1,100)
        print(numero)
        lista_numeros.append(numero)
    for numero in lista_numeros:
        repetidos(lista_numeros)
    
def main():
    
    listado_palabras = []
    lista_palabras_1(listado_palabras)
    repetidos(listado_palabras)
    numeros_aleatorios(repetidos)
    
if __name__ == "__main__":
    main()