def lista_palabras_1(listado_palabras_1):
    
    print("Lista 1:") 
    while True:
        palabras = input("Ingrese una palabra (o 'fin' para terminar): ")
        if palabras.lower() == 'fin':
            break
        listado_palabras_1.append(palabras)
    return listado_palabras_1

def lista_palabras_2(listado_palabras_2):
    
    print("Lista 2:") 
    while True:
        palabras = input("Ingrese una palabra (o 'fin' para terminar): ")
        if palabras.lower() == 'fin':
            break
        listado_palabras_2.append(palabras)
    return listado_palabras_2

def escrituras(listado_palabras_1, listado_palabras_2):
    
    listado_palabras_1_no_rep = set(listado_palabras_1)
    listado_palabras_2_no_rep = set(listado_palabras_2)
    print("Palabras únicas en Lista 1:", listado_palabras_1_no_rep)
    print("Palabras únicas en Lista 2:", listado_palabras_2_no_rep)
    solo_en_lista_1 = listado_palabras_1_no_rep - listado_palabras_2_no_rep
    solo_en_lista_2 = listado_palabras_2_no_rep - listado_palabras_1_no_rep
    print(f"Palabras en Lista 1 y no en Lista 2: {solo_en_lista_1}")
    print(f"Palabras en Lista 2 y no en Lista 1: {solo_en_lista_2}")
    lista_nueva = listado_palabras_1 + listado_palabras_2
    print("Lista combinada:", lista_nueva)
    
def main():
    
    listado_palabras_1 = []
    listado_palabras_2 = []
    lista_palabras_1(listado_palabras_1)
    lista_palabras_2(listado_palabras_2)
    escrituras(listado_palabras_1,listado_palabras_2)
    
if __name__ == "__main__":
    main()