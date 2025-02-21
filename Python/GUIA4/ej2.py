vec1 = [] 
vec2 = [] 

def vector_1():

  print("vector 1: ")
  for _ in range(15):
      numeros = int(input("ingrese un numero: "))
      if numeros >= 0 and numeros <= 21:
        vec1.append(numeros)
      else:
        while numeros < 0 or numeros > 21:
          numeros = int(input("porfavor, ingrese un numero positivo menor a 21: "))
          if numeros >= 0 and numeros <= 21:
            vec1.append(numeros)
  vec1.sort()
  print("")
  print(f"vector 1: {vec1}")
  
def vector_2():

  for numeros in range(len(vec1)):
      numeros = vec1[numeros] * vec1[numeros]
      vec2.append(numeros)
      vec2.sort()
  print("")
  print(f"vector 2: {vec2}")

def matriz():

  print("")
  print("Matriz:")
  for valor1, valor2 in zip(vec1, vec2):  
        print(valor1, valor2)
        
def num_rep():
    
  numeros = ["0","1","2","3","4","5","6","7","8","9"]
  numeros_repetidos = []
  for numeros in vec1 and vec2:
    if numeros in vec1 and vec2:
        numeros_repetidos.append(numeros)
        num_repetido = numeros_repetidos.count(numeros)
  print(f"el numero mas repetido es: {num_repetido}") 
       
vector_1()
vector_2()
matriz()
num_rep()