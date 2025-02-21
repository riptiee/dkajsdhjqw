def vector(lista_num):
    
    while True:
        try:
            numero = int(input("Ingresa un número o un caracter para finalizar: "))
            lista_num.append(numero)
        except ValueError:
            break
    print(lista_num)

def fibonacci_trucho(lista_numeros):

  lista_nueva = [lista_numeros[0]]
  for numero in range(1, len(lista_numeros)):
        numero_sum = lista_nueva[-1] + lista_numeros[numero]
        lista_nueva.append(numero_sum)
  print(lista_nueva)

def main():
    
    lista_num = []
    vector(lista_num)
    fibonacci_trucho(lista_num)
    
if __name__ == "__main__":
    main()