
def conversion(libras):
    kg = libras * 0.453592
    peso_redondeado = round(kg, 1)
    return peso_redondeado

numero = int(input("Ingrese cuántas libras desea convertir a kilogramos: "))
resultado = conversion(numero)
print(f"Las libras redondeadas son {resultado} kilogramos.")



    