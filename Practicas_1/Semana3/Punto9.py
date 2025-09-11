numeros = [0] * 10

for i in range(10):
    numeros[i] = int(input("Ingrese un número: "))

for i in range(10):
    if numeros[i] % 2 == 0:
        numeros[i] = 0

print("Array resultante:")
for i in range(10):
    print(numeros[i])
