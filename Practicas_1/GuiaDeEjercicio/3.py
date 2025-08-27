def area_triangulo(base, altura):
    return (base * altura) / 2

b = float(input("Ingresa la base del triángulo: "))
h = float(input("Ingresa la altura del triángulo: "))

resultado = area_triangulo(b, h)
print("El área del triángulo es:", resultado)
