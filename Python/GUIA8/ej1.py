import random

def es_secuencia_valida(secuencia):

    if all(x == secuencia[0] for x in secuencia):
        return True

    elif all(secuencia[i] == secuencia[i-1] + 1 for i in range(1, len(secuencia))):
        return True
    return False

def verifica_secuencia(matriz, n):
    filas = len(matriz)
    columnas = len(matriz[0])

    for i in range(filas):
        for j in range(columnas - n + 1):
            secuencia = matriz[i][j:j+n]
            if es_secuencia_valida(secuencia):
                return True

    for j in range(columnas):
        for i in range(filas - n + 1):
            secuencia = [matriz[i+k][j] for k in range(n)]
            if es_secuencia_valida(secuencia):
                return True

    for i in range(filas - n + 1):
        for j in range(columnas - n + 1):
            secuencia = [matriz[i+k][j+k] for k in range(n)]
            if es_secuencia_valida(secuencia):
                return True

    for i in range(filas - n + 1):
        for j in range(n - 1, columnas):
            secuencia = [matriz[i+k][j-k] for k in range(n)]
            if es_secuencia_valida(secuencia):
                return True

    return False

matriz = []
for i in range(3):
    fila = [random.randint(1, 9) for _ in range(3)]
    matriz.append(fila)

print("Matriz generada:")
for fila in matriz:
    print(fila)

n = 3

if verifica_secuencia(matriz, n):
    print("Hay una secuencia válida en la matriz (consecutiva o del mismo número).")
else:
    print("No hay una secuencia válida en la matriz.")

