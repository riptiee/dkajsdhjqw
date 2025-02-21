import random, numpy as np

def contador_ocurrencias(matriz):
  while True:
    ocurrencias = 0
    elemento = int(input("Ingrese el elemento que desea saber sus ocurrencias: "))
    
    for fila in matriz:
        for e in fila:
            if e == elemento:
                ocurrencias += 1
    
    print(f"El número de ocurrencias del elemento {elemento} es: {ocurrencias}")
    print("")
    continuar = input("Desea ingresar otro elemento? ").lower()
    if continuar == "si":
      continue
    else:
      break
    
def tabla():
    matriz = []
    while len(matriz) < 25:
        numero = random.randint(1, 9)
        matriz.append(numero)
    matriz_np = np.array(matriz).reshape(5, 5)
    
    print("Tabla generada:")
    print(matriz_np)
    
    return matriz_np.tolist()

def main():
    matriz = tabla()  
    contador_ocurrencias(matriz)  

if __name__ == "__main__":
    main()

