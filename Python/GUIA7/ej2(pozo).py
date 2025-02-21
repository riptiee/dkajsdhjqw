import random, numpy as np
def PozoMillonario(tabla):
  
  while len(tabla) < 15:
    numero = random.randint(1, 25)
    if numero not in tabla:
        tabla.append(numero)
  tabla.sort()
  print("Tabla del Pozo Millonario:")
  for i in range(3):
    fila = tabla[i*5:(i+1)*5]
    print(np.array(fila))

def main():
   tabla = []
   PozoMillonario(tabla)

if __name__ == "__main__":
  main()
  
  
