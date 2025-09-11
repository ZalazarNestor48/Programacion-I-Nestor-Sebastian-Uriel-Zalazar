def buscar_valor(numeros, valor):
    for i in range(len(numeros)):
        if numeros[i] == valor:
            return i
    return -1


numeros = [0] * 8
for i in range(8):
    numeros[i] = int(input("Ingrese un número: "))

valor = int(input("Ingrese el número a buscar: "))
pos = buscar_valor(numeros, valor)

if pos != -1:
    print("El número se encuentra en la posición:", pos)
else:
    print("El número no se encuentra en el array.")
