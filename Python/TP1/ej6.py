#Ejercicio. Simular 5 tiradas de un dado. Para eso hacer primero un procedimiento que simule tirar un dado y muestre el número que salió.
#En el programa principal llamar a ese procedimiento 5 veces para simular que se tiran 5 dados
import random 
import time

def tiradas_dados():
    dado = random.randint(1,6)
    print("tirando un dado")
    for _ in range(5):
        print(".")
        time.sleep(0.8)
    print(f"ha caido el numero {dado}")
    print("---------------------")
        
for _ in range(5):
    tiradas_dados()
