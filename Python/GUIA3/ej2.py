#2

lista_nacionalidad = []
lista_pasajeros = []
ciudades = []
dniXciudad = []
dniXpais = []

def pasajeros():
 boletos = int(input("Cuantos pasajeros son: "))
 for _ in range(boletos):
  pasajeros = input("Ingrese el nombre del pasajero: ")
  dni = input("Ingrese el dni del pasajero: ")
  while len(dni) <8 or len(dni) >8:
   print("Porfavor, ingrese un dni verdadero")
   dni = input("Ingrese de nuevo el dni: ")
  destino = input("Ingrese el destino del pasajero: ")
  ciudad = input("Ingrese de que ciudad es el pasajero: ")
  ciudades.append(ciudad)
  pais = input("Ingrese de que pais es el pasajero: ")

  lista_pasajeros.append((pasajeros , dni , destino))
  lista_nacionalidad.append((ciudad , pais))
  dniXciudad.append((dni , ciudad))
  dniXpais.append((dni , pais))
  print(f"Datos del pasajero: {lista_pasajeros}")
  print(f"Nacionalidad del pasajero: {lista_nacionalidad}")

def menu_iterativo():

  opcionA = 1
  opcionB = 2
  opcionC = 3
  opcionD = 4
  opcionE = 5
  opcionF = 6
  opcionG = 0
  print("")
  print("""                    ~~   MENU   ~~
                  ~~   ITERATIVO  ~~

  Si desea agregar pasajeros a la lista de viajeros ingresar 1
  Si desea agregar ciudades a la lista de ciudades ingresar 2
  Si desea ver a qué ciudad viaja el pasajero ingresar 3
  Para mostrar la cantidad de pasajeros que viajan a alguna ciudad ingresar 4
  Para ver a qué país viaja un pasajero ingresar 5
  Para mostrar cuántos pasajeros viajan a un pais ingresar 6

  """)

  numero = int(input("Ingrese alguna opcion: "))

  if numero == opcionA: #✓
    boletos_2 = int(input("Ingrese cuantos pasajeros va a agregar: "))
    for _ in range(boletos_2):
      pasajeros = input("Ingrese el nombre del pasajero: ")
      dni = input("Ingrese el dni: ")
      while len(dni) <8 or len(dni) >8:
       print("Porfavor, ingrese un dni verdadero")
       dni = input("Ingrese de nuevo el dni: ")
      destino = input("Ingrese el destino del pasajero: ")
      ciudad = input("Ingrese de que ciudad es el pasajero: ")
      pais = input("Ingrese de que pais es el pasajero: ")

      dniXciudad.append((dni , ciudad))
      lista_pasajeros.append((pasajeros , dni , destino))
      lista_nacionalidad.append((ciudad , pais))
      print(f"{pasajeros} fue agregado a la lista de pasajeros")
      print(f"Datos de los pasajeros: {lista_pasajeros}")
      print(f"Nacionalidad del pasajero: {lista_nacionalidad}")

  if numero == opcionB: #✓
    num = int(input("Ingrese cuantas ciudades quiere ingresar: "))
    for _ in range(num):
      ciudad = input("Ingrese una ciudad: ")
      ciudades.append(ciudad)
      print(ciudades)

  if numero == opcionC: #✓
    dni = (input("Ingrese un DNI: "))
    if dni == dniXciudad[0][0]:
      print(f"El pasajero va hacia la ciudad: {dniXciudad[0][1]}")
    else:
      print("Ese dni no esta registrado")

  if numero == opcionD: #✓
    destino = input("Ingrese una ciudad: ")
    cantidad_pasajeros = sum(1 for pasajero in lista_pasajeros if pasajero[2] == destino)
    print(f"La cantidad de pasajeros que van a {destino} son: {cantidad_pasajeros}")

  if numero == opcionE: #✓
    dni = (input("Ingrese un DNI: "))
    if dni == dniXpais[0][0]:
      print(f"El pasajero va hacia el pais: {dniXpais[0][1]}")
    else:
       print("Ese dni no esta registrado")

  if numero == opcionF: #✓
    pais = input("Ingrese un país: ")
    cantidad_pasajeros = sum(1 for nacionalidad in lista_nacionalidad if nacionalidad[1] == pais)
    print(f"La cantidad de pasajeros que viajan al país {pais} son: {cantidad_pasajeros}")

  if numero == opcionG: #✓
    print("Hasta luego.")

pasajeros()
menu_iterativo()