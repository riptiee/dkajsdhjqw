import collections
def capicua():
  
  palabra = input("ingrese algunas palabras: ")
  while len(palabra) > 5 or len(palabra) < 5:
    print(f"alguna palabra ingresada no cumplio los terminos.")
    palabra = input("ingrese algunas palabras: ")

  counts = collections.Counter(palabra)
  is_capicua = True
  for i in range(len(palabra) // 2):
    if palabra[i] != palabra[len(palabra) - i - 1]:
      is_capicua = False
      break

  if is_capicua:
    print("si")
  else:
    print("no")
    
capicua()