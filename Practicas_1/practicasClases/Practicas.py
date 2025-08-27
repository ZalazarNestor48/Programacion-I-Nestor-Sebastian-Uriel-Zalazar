# Parque de Diversiones - PythonLand

# Ingreso de datos
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))

print("Atracciones disponibles:")
print("1. Montaña Rusa ($1500)")
print("2. Casa del Terror ($1200)")
print("3. Carrusel ($800)")

cantidad = int(input("¿Cuántas atracciones quiere usar? "))

# Variables de control
total = 0
contador = 0
atracciones_elegidas = ""
atracciones_validas = ""


while contador < cantidad:
    opcion = int(input("Elija una atracción (1-3): "))

    if opcion == 1:
        atracciones_elegidas += "Montaña Rusa, "
        if edad >= 12:
            total += 1500
            atracciones_validas += "Montaña Rusa, "
        else:
            print("No puede subir a la Montaña Rusa (solo 12 años o más).")

    elif opcion == 2:
        atracciones_elegidas += "Casa del Terror, "
        if edad >= 6:
            total += 1200
            atracciones_validas += "Casa del Terror, "
        else:
            print("No puede entrar a la Casa del Terror (solo 6 años o más).")

    elif opcion == 3:
        atracciones_elegidas += "Carrusel, "
        total += 800
        atracciones_validas += "Carrusel, "

    else:
        print("Opción inválida, intente nuevamente.")
        contador -= 1   # para que no cuente esta vuelta

    contador += 1

# Resultados
print("--- RESUMEN DE COMPRA ---")
print("Visitante:", nombre)
print("Edad:", edad)
print("Atracciones elegidas:", atracciones_elegidas[:-2])
print("Atracciones permitidas:", atracciones_validas[:-2])
print("Costo total a pagar: $", total)
