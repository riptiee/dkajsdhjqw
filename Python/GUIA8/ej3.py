tendencias = {
    '08-22-2016': {'#TN', '#Tecnica', '#POP'},
    '08-25-2016': {'#POP', '#Argentina'},
    '08-27-2016': {'#TN', '#BBC', '#Martes'}
}

def cuentaTopics(tendencias, listaFechas):
    contador = {}
    for fecha in listaFechas:
        if fecha in tendencias:
            for etiqueta in tendencias[fecha]:
                contador[etiqueta] = contador.get(etiqueta, 0) + 1
    return contador

def reportaTrending(tendencias, listaFechas):
    etiquetas_comunes = set.intersection(*(tendencias[fecha] for fecha in listaFechas if fecha in tendencias))
    etiquetas_al_menos_una = set.union(*(tendencias[fecha] for fecha in listaFechas if fecha in tendencias))
    
    print("Etiquetas en todos los días:", etiquetas_comunes)
    print("Etiquetas en al menos un día:", etiquetas_al_menos_una)

def reportaTrending_fechas(tendencias, fecha1, fecha2):
    etiquetas_fecha1 = tendencias.get(fecha1, set())
    etiquetas_fecha2 = tendencias.get(fecha2, set())
    solo_una_fecha = etiquetas_fecha1.symmetric_difference(etiquetas_fecha2)
    
    print("Etiquetas en solo una de las fechas:", solo_una_fecha)

listaFechas = ['08-22-2016', '08-25-2016', '08-27-2016']
print("Conteo de etiquetas:", cuentaTopics(tendencias, listaFechas))

print("\nReporte de tendencias:")
reportaTrending(tendencias, listaFechas)

print("\nTendencias en fechas específicas:")
reportaTrending_fechas(tendencias, '08-22-2016', '08-25-2016')
