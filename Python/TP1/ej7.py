#Ejercicio. Un restaurante está necesitando un sistema electrónico para mostar el menú a sus comensales.
#Se le deberá pedir al usuario que nos diga qué parte de la carta quiere
#(ej: tartas, parrilla, guarniciones, pastas, postres, bebidas) y, dependiendo de lo ingresado, se deberán imprimir sólo los platillos de la categoría elegida.
#Se deberán armar procedimientos separados que impriman cada sección de la carta.
#El usuario también puede ingresar la opción "completo" en cuyo caso se deberán mostrar todas las secciones del menú,
#agregando el título de cada sección antes de listar los items de la misma. Esto también debe hacerse en un procedimiento.
#Deberán hacerse al menos dos categorías de la carta, y en cada categoría deberán mostrarse al menos tres platos y/o bebidas.
import time
print("que parte del menu quiere: entrada, plato principal, postre o completo:")
plato = input("")
entrada = []

def entradas():
    print("este es el menu de entrada: ")
    time.sleep(1.5)
    print("bocaditos de ricota")
    time.sleep(0.8)
    print("huevos duros")
    time.sleep(0.8)
    print("tartita de espinaca")
    
def plato_principal():
    print("este es el menu del plato principal: ")
    time.sleep(1.5)
    print("milanesa napolitana con fritas")
    time.sleep(0.8)
    print("pizza napolitana")
    time.sleep(0.8)
    print("empanadas")
    
def postre():
    print("estos son los postres: ")
    time.sleep(1.5)
    print("helados de: menta granizada, chocolate blanco, y limon")
    time.sleep(0.8)
    print("flan con o sin crema")
    time.sleep(0.8)
    print("cheesecake")
    
def completo():
     entradas()
     plato_principal()
     postre()
    
if plato == "entrada":
    entradas()
    
if plato == "plato principal":
    plato_principal()
    
if plato == "postre":
    postre()

if plato == "completo":
    completo()
        
        