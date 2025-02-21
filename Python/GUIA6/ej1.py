#Ejercicio 1: Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'},
#pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.

def dinero():
    divisa = {
        'euro': '€',
        'dollar': '$',
        'yen': '¥'
    }
    pregunta = input("Ingrese alguna divisa para ver su simbolo: ").lower()
    
    if pregunta in divisa:
        print(f"El simbolo del {pregunta} es: {divisa[pregunta]}")
    else:
        print("La divisa ingresada no se encuentra en el diccionario")
        
def main():
    dinero()

if __name__ == "__main__":
    main()
