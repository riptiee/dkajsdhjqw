def vuelos():
    vuelo = 1
    movimientos={
        "vuelo" : [],
        "destino": [],
        "asientos": 100,
        }
    pasajeros={
        "pasajeroNro" : [],
        "abono" : 200,
    }
    
    while True:
        try:
            pasajes = int(input("Ingrese cuantos pasajeros viajan:"))
            if pasajes >100:
                print("Saquen a alguno.")
            else:
              movimientos["vuelo"] = vuelo
              movimientos["destino"] = input("Ingrese el destino del vuelo: ")
              abono = pasajes * pasajeros["abono"]
              print(f"""
                  Nro de vuelo:{movimientos["vuelo"]}, Destino:{movimientos['destino']}
                  Nro de pasaporte              Importe en US""")
              for p in range(pasajes):
               p += 1
               pasajeros["pasajeroNro"] = p
               print(f"                  {pasajeros['pasajeroNro']}                             {pasajeros['abono']}")   
               print(f"""
                  total recaudado del vuelo:{abono}
                  promedio de asientos libres:{movimientos['asientos'] - pasajes}
                  promedio de asientos ocupados:{pasajes}
                  """)
              vuelo += 1
              pregunta = input("Desea ingresar otro vuelo? ").lower()
              if pregunta == "si":
                  continue
              else:
                  break
        except ValueError:
            pass
    
def main():
    vuelos()

if __name__ == "__main__":
    main()    