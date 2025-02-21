import random
def tienda():
    
    mercado = {
        "remera" : [15000,f"STOCK:{random.randint(0,500)}"],
        "jean" : [25000,f"STOCK:{random.randint(0,500)}"],
        "campera" : [30000,f"STOCK:{random.randint(0,500)}"],
        "zapatillas" : [100000,f"STOCK:{random.randint(0,500)}"],
        "medias" : [900,f"STOCK:{random.randint(0,500)}"], 
    }
    
    empresa = {
        "sucursal_1" : random.randint(0,5000),
        "sucursal_2" : random.randint(0,5000),
        "sucursal_3" : random.randint(0,5000),
        "sucursal_4" : random.randint(0,5000),
    }
    
    recaudacion_S1 = (empresa['sucursal_1'] // 5) * (mercado['campera'][0]+mercado['medias'][0]+mercado['remera'][0]+mercado['jean'][0]+mercado['zapatillas'][0])
    recaudacion_S2 = (empresa['sucursal_2'] // 5) * (mercado['campera'][0]+mercado['medias'][0]+mercado['remera'][0]+mercado['jean'][0]+mercado['zapatillas'][0])
    recaudacion_S3 = (empresa['sucursal_3'] // 5) * (mercado['campera'][0]+mercado['medias'][0]+mercado['remera'][0]+mercado['jean'][0]+mercado['zapatillas'][0])
    recaudacion_S4 = (empresa['sucursal_4'] // 5) * (mercado['campera'][0]+mercado['medias'][0]+mercado['remera'][0]+mercado['jean'][0]+mercado['zapatillas'][0])
    recSucursales = {"sucursal 1":recaudacion_S1,"sucursal 2":recaudacion_S2,"sucursal 3":recaudacion_S3,"sucursal 4":recaudacion_S4}
    sucursal_pro = max(recSucursales,key=recSucursales.get)
    
    print(f"""
          el stock de cada articulo en todas las sucursales son: 
          remeras: {mercado['remera'][1]} 
          jean: {mercado['jean'][1]}
          campera: {mercado['campera'][1]}
          zapatillas: {mercado['zapatillas'][1]}
          medias: {mercado['medias'][1]}
          """)
    print(f"""
          la cantidad de articulos vendidos en la sucursal 2 son: {empresa['sucursal_2']}
          la cantidad del articulo 3 en la sucursal 1 son: {mercado['campera'][1]}
          """)
    print(f"""
          la recaudacion total de cada sucursales es:
          sucursal 1: ${recaudacion_S1}
          sucursal 2: ${recaudacion_S2}
          sucursal 3: ${recaudacion_S3}
          sucursal 4: ${recaudacion_S4}
          """)
    print(f"""
          la recaudacion de la empresa es: ${recaudacion_S1 + recaudacion_S2 + recaudacion_S3 + recaudacion_S4}
          la sucursal de mayor recaudacion es {sucursal_pro}
          """)
    
def main():
    tienda()
    
if __name__ == "__main__":
    main()