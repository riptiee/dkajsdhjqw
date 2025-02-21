lista_primaria = []
lista_secundaria = []
def alumnos_primaria():
    nombres_primaria = input("ingrese z para agregar nombres de alumnos del primario: ")
    if nombres_primaria == "z":
        while nombres_primaria != "x":
          nombres_primaria = input("ingrese un nombre: ")
          lista_primaria.append(nombres_primaria)
    else:
        print("xd")

def alumnos_secundaria():
    nombres_secundaria = input("ingrese z para agregar nombres de alumnos del secundario: ")
    if nombres_secundaria == "z":
        while nombres_secundaria != "x":
          nombres_secundaria = input("ingrese un nombre: ")
          lista_primaria.append(nombres_secundaria)

alumnos_primaria()
alumnos_secundaria()
lista_primaria_no_rep = set(lista_primaria)
lista_secundaria_no_rep = set(lista_secundaria)
print(lista_primaria_no_rep)
print(lista_secundaria_no_rep)