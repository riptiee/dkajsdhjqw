def dar_vuelta_parrafo(parrafo):
    
    parrafo_dado_vuelta = ""
    for i in range(len(parrafo) - 1, -1, -1):
        parrafo_dado_vuelta += parrafo[i]
    return parrafo_dado_vuelta

parrafo = input("Ingrese un párrafo: ")
parrafo_dado_vuelta = dar_vuelta_parrafo(parrafo)
print("El párrafo dado vuelta es:", parrafo_dado_vuelta)