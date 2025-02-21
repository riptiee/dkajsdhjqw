#Realizar un ejercicio que permita el ingreso de números de 5 dígitos, en un
#vector, hasta que uno de ellos sea negativo. Al finalizar el ingreso el programa deberá
#descomponer los números, agrupando los dígitos pares en un vector y los impares en
#otro, es decir que si se tiene el número 12345, se separan los valores 24 por un lado y
#135 por el otro. Finalizada dicha operación se deben mostrar los resultados de las
#sumas de los números de estos últimos vectores por posiciones contiguas
sumaVectores = []
numeros = []
pares = []
impares = []

def vector():
    
    while True:
        try:
            numero = int(input("Ingresa un número: "))
            if numero < 0:
                break
            elif 10000 <= numero <= 99999:
                numeros.append(numero)
            else:
                print("El número ingresado no tiene 5 dígitos, intente de nuevo.")
        except ValueError:
            print("Por favor, ingrese un número entero.")
    print(numeros)
     
def descomponer_numeros(numeros):

    for numero in numeros:
        while numero > 0:
            digito = numero % 10
            if digito % 2 == 0:
                pares.append(digito)
            else:
                impares.append(digito)
            numero //= 10
    
    print(pares, impares) 

def suma_contigua():
    
    for num in zip(pares,impares):
        if pares[0] == 0: 
           num = impares[-1]
           sumaVectores.append(num)
        if impares[0] == 0:
            num = pares[-1]
            sumaVectores.append(num)
        else:
           num = pares[-1] + impares[-1]
        sumaVectores.append(num)
        pares.pop(-1) and impares.pop(-1)
    print(sumaVectores) 

vector()
descomponer_numeros(numeros)
suma_contigua()