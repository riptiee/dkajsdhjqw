import random

cuantos1 = 0
cuantos2 = 0
cuantos3 = 0
cuantos4 = 0
cuantos5 = 0
cuantos6 = 0

print("TIRADA DE DADOS")
print("")
for _ in range(10):  
  dado = random.randint(1, 6)
  print(dado)

  if dado == 1:
    cuantos1 = cuantos1 + 1
  if dado == 2:
    cuantos2 = cuantos2 + 1
  if dado == 3:
    cuantos3 = cuantos3 + 1
  if dado == 4:
    cuantos4 = cuantos4 + 1
  if dado == 5:
    cuantos5 = cuantos5 + 1
  if dado == 6:
    cuantos6 = cuantos6 + 1

print()
print(f"Entre los 10 dados salieron {cuantos1} números uno")
print(f"Entre los 10 dados salieron {cuantos2} números dos")
print(f"Entre los 10 dados salieron {cuantos3} números tres")
print(f"Entre los 10 dados salieron {cuantos4} números cuatro")
print(f"Entre los 10 dados salieron {cuantos5} números cinco")
print(f"Entre los 10 dados salieron {cuantos6} números seis")
print()