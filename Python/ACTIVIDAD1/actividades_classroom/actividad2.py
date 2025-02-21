#Pedir 6 numeros y decir si hubo alguna que fuera negativo

for numeros in range (6):
  n = int(input("escriba un numero: "))
  if (n<0): 
   print("hay almenos un numero negativo")
  else:
   print("no hay ningun numero negativo")
 
 