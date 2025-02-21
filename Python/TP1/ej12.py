import math

def circunferencia(diametro):
   circulo = 3.14 * float(diametro)
   circulo_redondeado = round(circulo, 1)
   return circulo_redondeado

numero = int(input("ingrese un diametro: "))
resultado = circunferencia(numero)
print(f"el perimetro del diametro dado es {resultado}")