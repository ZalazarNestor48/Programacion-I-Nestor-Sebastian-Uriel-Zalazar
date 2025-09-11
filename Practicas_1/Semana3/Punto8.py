a = [0] * 5
b = [0] * 5

print("Ingrese los valores del primer array:")
for i in range(5):
    a[i] = int(input())

print("Ingrese los valores del segundo array:")
for i in range(5):
    b[i] = int(input())

iguales = True
for i in range(5):
    if a[i] != b[i]:
        iguales = False
        break

if iguales:
    print("Los arrays son iguales.")
else:
    print("Los arrays no son iguales.")
