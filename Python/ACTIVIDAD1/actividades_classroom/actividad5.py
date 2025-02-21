import random

print('             "tira los dados"')
print("-------------------------------------------")

seEncontro = False

for d in range (5):
  dado1 = random.randint (1,6)
  dado2 = random.randint (1,6)

  dado3 = dado1 + dado2

  print("te tocaron" , dado1,"y", dado2,"la suma de estos dados da", dado3)
  if dado3 == 7:
    seEncontro = True
    print("!felicidades!")
  else:
    print("mala suerte papu")