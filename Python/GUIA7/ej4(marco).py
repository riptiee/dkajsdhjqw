def main():
    
  filas = int(input("Ingrese la cantidad de filas del marco: "))
  columnas = int(input("Ingrese la cantidad de columnas del marco: "))
  marco = [[0 for _ in range(columnas)] for _ in range(filas)]

  for i in range(filas):
    for j in range(columnas):
        if i == 0 or i == filas-1 or j == 0 or j == columnas-1:
            marco[i][j] = 1

  for fila in marco:
    print(''.join(map(str, fila)))
    
if __name__ == "__main__":
    main()