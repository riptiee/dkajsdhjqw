import random,numpy as np
 
def tabla():
    matriz = []
    while len(matriz) < 9:
        numero = random.randint(1, 50)
        matriz.append(numero)
    matriz_np = np.array(matriz).reshape(3, 3)
    
    print("Tabla generada:")
    print(matriz_np)
    matriz_lista = matriz_np.flatten()

    if len(matriz_lista) != len(set(matriz_lista)):
        print(True)
    else:
        print(False)
        
    return matriz_np.tolist()
        
def main():
    tabla()  

if __name__ == "__main__":
    main()