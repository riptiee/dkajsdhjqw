#Ejercicio 2: Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario.
#Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.

def datos():
    
    user_data = {
        
    }
    
    user_data["nombre"] = input("Ingrese su nombre y apellido: ")
    user_data["edad"] = int(input("Ingrese su edad: "))
    user_data["direccion"] = input("Ingrese su direccion: ")
    user_data["telefono"] = input("Ingrese su telefono: ")
    
    print(f"{user_data['nombre']} tiene {user_data['edad']} años, vive en {user_data['direccion']} y su numero de telefono es {user_data['telefono']}")
    
def main():
    datos()
    
if __name__ == "__main__":
    main()