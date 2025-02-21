import random,numpy as np

def campeonato(equipos):
    puntos = [0, 1, 3]
    torneo = []

    for _ in range(equipos):
      torneo.append([None] * equipos)

    for e in range(equipos):
      for p in range(equipos):
        if e == p:
           torneo[e][p] = 'x'
        elif torneo[e][p] == None:
            resultado = random.choice(puntos)
            torneo[e][p] = resultado
            torneo[p][e] = resultado
    
    print(np.array(torneo))

def main():
    while True:
      try:
        equipos = int(input("Ingrese cuantos equipos van a ser para el campeonato: "))
        if equipos >= 2 and equipos <= 10:
          break
        else:
          print("Por favor, ingrese un número entre 2 y 10.")
      except ValueError:
          print("Por favor, intente de nuevo.")
    campeonato(equipos)

if __name__ == "__main__":
    main()