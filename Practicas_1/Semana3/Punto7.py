numeros = [0] * 6

for i in range(6):
    numeros[i] = int(input("Ingrese un número: "))

print("Array invertido:")
for i in range(5, -1, -1):
    print(numeros[i])
