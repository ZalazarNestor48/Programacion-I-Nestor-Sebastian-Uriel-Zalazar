numeros = [0] * 7

for i in range(7):
    numeros[i] = int(input("Ingrese un número: "))

mayor = numeros[0]
posicion = 0

for i in range(1, 7):
    if numeros[i] > mayor:
        mayor = numeros[i]
        posicion = i

print("El mayor es:", mayor, "y está en la posición:", posicion)
