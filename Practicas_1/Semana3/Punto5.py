numeros = [0] * 10

for i in range(10):
    numeros[i] = int(input("Ingrese un número: "))

buscar = int(input("Ingrese el número a buscar: "))
posicion = -1

for i in range(10):
    if numeros[i] == buscar:
        posicion = i
        break

if posicion != -1:
    print("El número se encuentra en la posición:", posicion)
else:
    print("El número no se encuentra en el array.")
