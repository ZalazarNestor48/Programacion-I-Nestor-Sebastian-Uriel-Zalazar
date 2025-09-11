numeros = [0.0] * 6
suma = 0

for i in range(6):
    numeros[i] = float(input("Ingrese un número real: "))
    suma = suma + numeros[i]

promedio = suma / 6
print("El promedio es:", promedio)
