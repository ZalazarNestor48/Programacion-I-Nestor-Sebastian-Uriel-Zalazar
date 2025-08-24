# Práctica Semana 1 - Parque de Diversiones PythonLand

# 1. Ingreso de datos
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))

print("\nAtracciones disponibles:")
print("1. Montaña Rusa ($1500)")
print("2. Casa del Terror ($1200)")
print("3. Carrusel ($800)")

num_atracciones = int(input("¿Cuántas atracciones desea usar? "))

# Lista de atracciones disponibles con precios
atracciones = {
    "Montaña Rusa": 1500,
    "Casa del Terror": 1200,
    "Carrusel": 800
}

# 2 y 3. Uso de condicionales y ciclos
elegidas = []   # atracciones que el visitante quiere
permitidas = [] # atracciones que realmente puede usar
costo_total = 0

for i in range(num_atracciones):
    opcion = input(f"Ingrese el nombre de la atracción #{i+1}: ")

    if opcion not in atracciones:
        print(" Atracción no válida. Intente de nuevo.")
        continue
    
    elegidas.append(opcion)

    # Reglas según edad
    if edad < 6:
        if opcion == "Carrusel":
            permitidas.append(opcion)
            costo_total += atracciones[opcion]
        else:
            print(f" No puede usar {opcion}, solo puede usar el Carrusel.")
    elif edad < 12:
        if opcion == "Montaña Rusa":
            print(f" No puede usar {opcion}, necesita tener 12 años o más.")
        else:
            permitidas.append(opcion)
            costo_total += atracciones[opcion]
    else:
        permitidas.append(opcion)
        costo_total += atracciones[opcion]

# 4. Salida de resultados
print(" --- Resumen de visita --- ")
print(f"Visitante: {nombre}")
print(f"Edad: {edad} años")
print(f"Atracciones elegidas: {elegidas}")
print(f"Atracciones permitidas: {permitidas}")
print(f"Costo total a pagar: ${costo_total}")
