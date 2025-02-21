import random

def generarListaAleatoria(cantidadDeNumeros, valorMinimo, valorMaximo):
  tiradas = []
  for n in range(9):
    n = int(input("Elegí un número entre 0 y 36: "))
    tiradas.append(random.randint(valorMinimo, valorMaximo))
  return tiradas

def buscarValor(valorElegido, listaDeValores):
  seEncontro = False
  for valor in listaDeValores:
    if valor == valorElegido:
      seEncontro = True
  return seEncontro

numeroApostado = int(input("Elegí un número entre 0 y 36: "))
resultadosDeTiradasDeRuleta = generarListaAleatoria(10, 0, 36)
seGano = buscarValor(numeroApostado, resultadosDeTiradasDeRuleta)
if seGano:
  print("Ganaste, uno de los dados dio en el blanco!")
else:
  print("Segui participando papu...")