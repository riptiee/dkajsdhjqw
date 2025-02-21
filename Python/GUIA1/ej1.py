def cif_program():
  
  num = int(input(f"ingrese un numero: "))
  while len(str(num)) > 6 or len(str(num)) < 6:
    print(f"El número {num} no tiene 6 cifras. Por favor, ingrese un número de 6 cifras.")
    num = int(input(f"ingrese un numero: "))
  cifras = [int(c) for c in str(num)]
  sumatoria_pares = sum(c for c in cifras if c % 2 == 0)
  print(f"La suma de los dígitos pares de {num} es {sumatoria_pares}")
  
cif_program()