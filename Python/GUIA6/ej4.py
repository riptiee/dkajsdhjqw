#Ejercicio 4: Escribir un programa que pregunte una fecha en formato dd/mm/aaaa 
#y muestre por pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes> es el nombre del mes.

def calendario():
    
    fichero = []
    while True:
        try:
          fecha = input("Ingrese una fecha de formato completo: ")
          if fecha.split(" ") == 3 and fecha[0] <= 2 and fecha[1] <= 2 and fecha[2] <= 4:
              fichero.append((fecha[0]),(fecha[1]),(fecha[2]))
              break
          else:
              print("Porfavor, ingrese las fechas correctamente.")
        except ValueError:
            print("dea")
    
def main():
    calendario()
    
if __name__ == "__main__":
    main()