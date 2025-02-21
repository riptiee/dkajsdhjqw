agenda = {}

def buscar_o_modificar(nombre):
    if nombre in agenda:
        print(f"Teléfono actual: {agenda[nombre]}")
        opcion = input("¿Deseas modificar el número? (s/n): ")
        if opcion.lower() == 's':
            nuevo_telefono = input("Ingrese el nuevo número: ")
            agenda[nombre] = nuevo_telefono
            print("Número actualizado.")
    else:
        telefono = input("Nombre no encontrado. Ingresa el teléfono para añadir a la agenda: ")
        agenda[nombre] = telefono
        print("Contacto añadido.")

while True:
    nombre = input("Ingrese un nombre (o '*' para salir): ")
    if nombre == "*":
        break
    buscar_o_modificar(nombre)
