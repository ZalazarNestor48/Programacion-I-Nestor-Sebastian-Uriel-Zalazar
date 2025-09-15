
titulos = [""] * 20
ejemplares = [0] * 20
contador = 0  



def cargar_titulos(titulos, ejemplares, contador):
    """Permite ingresar hasta 20 títulos con su cantidad de ejemplares"""
    while contador < 20:
        titulo = input("Ingrese título (o 'fin' para terminar): ")
        if titulo == "fin":
            break
        copias = int(input("Cantidad de ejemplares: "))
        titulos[contador] = titulo
        ejemplares[contador] = copias
        contador += 1
    print("Carga finalizada.")
    return contador


def mostrar_catalogo(titulos, ejemplares, contador):
    """Muestra todos los títulos con su cantidad de ejemplares"""
    print("\n--- Catálogo completo ---")
    if contador == 0:
        print("No hay títulos cargados.")
    else:
        for i in range(contador):
            print(f"{titulos[i]} -> {ejemplares[i]} copias")


def consultar_disponibilidad(titulos, ejemplares, contador):
    """Permite buscar un título y ver cuántas copias tiene"""
    buscar = input("Ingrese el título a consultar: ")
    for i in range(contador):
        if titulos[i] == buscar:   
            print(f"{titulos[i]} tiene {ejemplares[i]} copias disponibles.")
            return
    print("Título no encontrado.")


def listar_agotados(titulos, ejemplares, contador):
    """Muestra los títulos que no tienen ejemplares disponibles"""
    print("\n--- Títulos agotados ---")
    encontrado = False
    for i in range(contador):
        if ejemplares[i] == 0:
            print(titulos[i])
            encontrado = True
    if not encontrado:
        print("No hay títulos agotados.")


def agregar_titulo(titulos, ejemplares, contador):
    """Agrega un nuevo título siempre que no se supere el límite"""
    if contador < 20:
        titulo = input("Nuevo título: ")
        copias = int(input("Cantidad de ejemplares: "))
        titulos[contador] = titulo
        ejemplares[contador] = copias
        contador += 1
        print("Título agregado correctamente.")
    else:
        print("Catálogo lleno (máx. 20 títulos).")
    return contador


def actualizar_ejemplares(titulos, ejemplares, contador):
    """Permite modificar la cantidad de ejemplares (préstamo o devolución)"""
    buscar = input("Ingrese el título a actualizar: ")
    for i in range(contador):
        if titulos[i] == buscar:   
            cambio = int(input("Ingrese la cantidad a sumar/restar: "))
            ejemplares[i] += cambio
            if ejemplares[i] < 0:
                ejemplares[i] = 0
            print(f"Nuevo total de {titulos[i]}: {ejemplares[i]} copias.")
            return
    print("Título no encontrado.")


while True:
    print("\n====== MENÚ ======")
    print("1. Cargar títulos y ejemplares")
    print("2. Mostrar catálogo completo")
    print("3. Consultar disponibilidad")
    print("4. Listar títulos agotados")
    print("5. Agregar un nuevo título")
    print("6. Actualizar ejemplares (préstamo/devolución)")
    print("7. Salir")

    opcion = input("Elija una opción: ")

    if opcion == "1":
        contador = cargar_titulos(titulos, ejemplares, contador)
    elif opcion == "2":
        mostrar_catalogo(titulos, ejemplares, contador)
    elif opcion == "3":
        consultar_disponibilidad(titulos, ejemplares, contador)
    elif opcion == "4":
        listar_agotados(titulos, ejemplares, contador)
    elif opcion == "5":
        contador = agregar_titulo(titulos, ejemplares, contador)
    elif opcion == "6":
        actualizar_ejemplares(titulos, ejemplares, contador)
    elif opcion == "7":
        print("Saliendo del sistema...")
        break
    else:
        print("Opción no válida, intente nuevamente.")
