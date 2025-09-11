numeros = [0] * 8
contador = 0

for i in range(8):
    numeros[i] = int(input("Ingrese un número: "))
    if numeros[i] > 100:
        contador = contador + 1

print("La cantidad de números mayores a 100 es:", contador)
