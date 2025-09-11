
numeros = [0] * 10
suma = 0


for i in range(10):
    numeros[i] = int(input("Ingrese un número: "))
    suma = suma + numeros[i]   


print("La suma de todos los elementos es:", suma)
