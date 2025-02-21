palabra = input('Ingrese una palabra: ')

seEncontro = False

for letra in palabra:
  if letra == "z" or letra == 'z':
    seEncontro = True

if seEncontro:
  print("Hay alguna z")
else:
  print("No hay z")