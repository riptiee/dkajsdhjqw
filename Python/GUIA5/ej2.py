#Ejercicio 2: Escriba un programa que permita crear una lista de palabras y que, a
#continuación, elimine los elementos repetidos (dejando únicamente el primero de los
#elementos repetidos)

def lista_palabras(listado_palabras):

    while True:
        palabras = input("Ingrese una palabra (o 'fin' para terminar): ")
        if palabras.lower() == 'fin':
            break
        listado_palabras.append(palabras)
    return listado_palabras

def eliminar_repetidos(listado_palabras):
    
    lista_rep = []
    for palabras in listado_palabras:
        repetidos = listado_palabras.count(palabras)
        if repetidos >1 :
            listado_palabras.remove(palabras)
            lista_rep.append(palabras)
    el_repetido = lista_rep[0]
    listado_palabras.append(el_repetido)
    for palabras in lista_rep:
        if lista_rep.count(palabras) >1:
            lista_rep.remove(palabras)
    print(listado_palabras)
    
def main():

  listado_palabras = []
  lista_palabras(listado_palabras)
  eliminar_repetidos(listado_palabras)

if __name__ == "__main__":
  main()