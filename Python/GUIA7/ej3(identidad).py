import numpy as np

def matriz():
    identidad = []
    for _ in range(5):
      identidad.append([None] * 5)
    for f in range(5):
      for c in range(5):
        if f == c:
           identidad[f][c] = 1
        else:
            identidad[f][c] = 0
            identidad[c][f] = 0
    print(np.array(identidad))

def main():
    matriz()

if __name__ == "__main__":
    main()