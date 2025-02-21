import random
def tirada_de_moneda():
  moneda = [1,2]
  apuesta = random.choice(moneda)
  if apuesta == 1:
    print("toco cara")
  else:
    print("toco ceca")

tirada_de_moneda()