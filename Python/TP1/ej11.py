
def conversion(farenheit):
    celcius = (farenheit - 32) * 5/9
    grado_redondeado = round(celcius, 1)
    return grado_redondeado

numero = int(input("Ingrese cuántos grados F desea convertir a grados C: "))
resultado = conversion(numero)
print(f"los grados F son covertidos en {resultado} grados C.")