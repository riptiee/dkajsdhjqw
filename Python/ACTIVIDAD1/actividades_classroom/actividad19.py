import random

for _ in range(15):
    dado1 = random.randint(1,6)
    dado2 = random.randint(1,6)
    print("------------------------------------")
    print(f"dado 1: {dado1}")
    print(f"dado 2: {dado2}")
    if dado1 == 1 and dado2 == 1:
     print("felicidades cayo doble 1")
    if dado1 == 6 and dado2 == 6:
     print("felicidades cayo doble 6")
