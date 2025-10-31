import random
from datos import cartas
from puntuacion import calcular_jugada
from archivos import guardar_puntaje


def tirar_dados():
    """Simula tirar 5 dados (campeones aleatorios de LoL)."""
    lista_dados = []
    for i in range(5):
        dado = random.choice(cartas)  # elige un campeón al azar
        lista_dados.append(dado)
    return lista_dados


def mostrar_dados(dados):
    """Muestra los 5 dados actuales (nombre y puntos)."""
    print("\nDados actuales:")
    for i in range(5):
        nombre = dados[i]["nombre"]
        puntos = dados[i]["puntos"]
        print(f"{i+1}. {nombre} ({puntos})")


def jugar():
    """Función principal del juego de consola."""
    print("\n--- NUEVA PARTIDA ---")
    nombre = input("Ingrese su nombre: ")

    puntos_totales = 0

    # 10 turnos por partida
    for turno in range(10):
        print(f"\n--- Turno {turno + 1} ---")
        print(f"Puntaje total actual: {puntos_totales}")

        # Primer tiro
        dados = tirar_dados()
        mostrar_dados(dados)

        # Hasta dos re-tiros
        for tiro in range(2):
            mantener = input("Ingrese los números de los dados que quiere mantener (ej: 1,3) o ENTER para tirar todos: ")

            # Si el jugador no mantiene ninguno, se tiran todos los dados
            if mantener == "":
                for i in range(5):
                    dados[i] = random.choice(cartas)

            else:
                # Revisamos uno por uno si el número del dado está dentro del texto que escribió el jugador
                for i in range(5):
                    numero_dado = str(i + 1)
                    if numero_dado not in mantener:
                        # Si no lo escribió, se vuelve a tirar ese dado
                        dados[i] = random.choice(cartas)

            mostrar_dados(dados)

        # Pedir categoría donde anotar puntaje
        categoria = input("Ingrese la categoría donde desea anotar el puntaje: ")
        puntos = calcular_jugada(dados, categoria)
        puntos_totales += puntos

        print(f"Puntaje obtenido en '{categoria}': {puntos}")
        print(f"Puntaje total hasta ahora: {puntos_totales}")

    # Fin del juego
    print("\n--- FIN DE LA PARTIDA ---")
    print(f"Puntaje final de {nombre}: {puntos_totales}")
    guardar_puntaje(nombre, puntos_totales)
