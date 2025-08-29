
def mostrar_atracciones():
    print("1. Montaña rusa - $50 (mínimo 12 años)")
    print("2. Rueda de la fortuna - $30 (sin restricción)")
    print("3. Casa del terror - $40 (mínimo 15 años)")

def puede_subir(edad, atraccion):
    if atraccion == 1 and edad < 12:
        return False
    if atraccion == 3 and edad < 15:
        return False
    return True

def calcular_precio(atraccion):
    precios = {1: 50, 2: 30, 3: 40}
    return precios.get(atraccion, 0)

def registrar_visita():
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))
    
    mostrar_atracciones()
    atracciones = list(map(int, input("Ingrese las atracciones elegidas (separadas por coma): ").split(",")))
    
    return {"nombre": nombre, "edad": edad, "atracciones": atracciones}

def mostrar_resumen(resumen):
    print("\n--- Resumen de visita ---")
    print("Nombre:", resumen["nombre"])
    print("Edad:", resumen["edad"])
    print("Atracciones elegidas:", resumen["atracciones"])
    print("Costo total:", resumen["costo_total"])
