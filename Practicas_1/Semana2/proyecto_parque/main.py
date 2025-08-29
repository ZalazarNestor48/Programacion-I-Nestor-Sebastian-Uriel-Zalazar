from proyecto_parque.parque import registrar_visita, puede_subir, calcular_precio, mostrar_resumen

def main():
    datos = registrar_visita()
    costo_total = 0
    atracciones_validas = []

    for a in datos["atracciones"]:
        if puede_subir(datos["edad"], a):
            costo_total += calcular_precio(a)
            atracciones_validas.append(a)
        else:
            print(f"No puede acceder a la atracción {a} por restricción de edad.")

    # Descuento del 10% si son 3 o más atracciones
    if len(atracciones_validas) >= 3:
        costo_total *= 0.9

    datos["costo_total"] = costo_total
    datos["atracciones"] = atracciones_validas
    mostrar_resumen(datos)

if __name__ == "__main__":
    main()

