def es_par(numero):
    return numero % 2 == 0

numero = int(input("Ingresa un número: "))

if es_par(numero):
    print("El número es par.")
else:
    print("El número es impar.")
