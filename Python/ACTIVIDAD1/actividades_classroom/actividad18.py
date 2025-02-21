vocales = "aeiouAEIOU"
consonantes = "bcdfghjklmnñpqrstvwxyzBCDFGHJKLMNÑPQRSTVXYZ"
pvocales = []
pconsonantes = []

palabra = input("ingrese una palabra: ")

for letra in palabra:
  if letra in vocales:
    pvocales.append(letra)
  if letra in consonantes:
    pconsonantes.append(letra)
    
print(f"la palabra ingresada: {palabra} contiene las vocales {pvocales} y las consonantes {pconsonantes}")