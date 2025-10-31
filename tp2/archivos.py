import csv

def guardar_puntaje(nombre, puntos):
    with open("puntajes.csv", "a", newline="") as f:
        escritor = csv.writer(f)
        escritor.writerow([nombre, puntos])

def mostrar_estadisticas():
    print("\n--- ESTADÍSTICAS ---")
    try:
        with open("puntajes.csv", "r") as f:
            lector = csv.reader(f)
            puntajes = sorted(lector, key=lambda x: int(x[1]), reverse=True)
            for i, (nombre, puntos) in enumerate(puntajes[:10], 1):
                print(f"{i}. {nombre}: {puntos} pts")
    except FileNotFoundError:
        print("No hay puntajes guardados aún.")

def mostrar_creditos():
    print("\n--- CRÉDITOS ---")
    print("Juego desarrollado por: [Tu nombre] y [Tu compañero]")
    print("Materia: Programación I - UTN")
    print("Año: 2025")
    print("Temática: League of Legends")
