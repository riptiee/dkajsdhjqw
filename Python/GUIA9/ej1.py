import random

def dieta(personas, productos):
    
    if personas["dinero disponible"] >= productos["precio"]:
        pass

def main():
    
    personas = {
        "nombre": input("Ingrese el nombre de la persona: "),
        "peso" : int(input("ingrese el peso de la persona: ")),
        "dinero disponible": int(input("ingrese el dinero disponible de la persona: "))
    }
    
    productos = {
        "descripcion" : input("Ingrese una descripcion breve del prodcuto: "),
        "precio" : int(input("ingrese el precio del producto: ")),
        "calorias" : int("ingrese las calorias del producto: "),
        "salud" : random.randint(1,5)
    }
 
    dieta(personas, productos)

if __name__ == "__main__":
    main()