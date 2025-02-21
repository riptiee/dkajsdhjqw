# dado con suspenso
import time
import random
print("Tirando un dado", end="")

for _ in range(5):
  print(".", end="")
  time.sleep(0.5)

dado = random.randint(1, 6)
print(f" salió un {dado}")