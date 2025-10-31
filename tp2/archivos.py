import os
import csv   

def guardar_puntaje(nombre, puntos):
   
    with open("puntajes.csv", "a", newline="") as f:
        escritor = csv.writer(f)
        escritor.writerow([nombre, puntos])
def mostrar_estadisticas():
    
    #Muestra los 10 mejores puntajes guardados en el archivo.
    #Si el archivo no existe, avisa al usuario.

    print("\n--- ESTADÍSTICAS ---")

    # Verificamos si el archivo existe antes de intentar abrirlo
    if not os.path.exists("puntajes.csv"):
        print("No hay puntajes guardados aún.")
        return

    # Abrimos el archivo en modo lectura
    with open("puntajes.csv", "r") as f:
        lector = csv.reader(f)
        puntajes = list(lector)  

        
        for i in range(len(puntajes)):
            for j in range(i + 1, len(puntajes)):
                # Comparamos los puntajes (índice 1)
                if int(puntajes[j][1]) > int(puntajes[i][1]):
                    puntajes[i], puntajes[j] = puntajes[j], puntajes[i]

        # Mostramos solo los primeros 10 puntajes
        for i, (nombre, puntos) in enumerate(puntajes[:10], 1):
            print(f"{i}. {nombre}: {puntos} pts")



def mostrar_creditos():

    print("\n--- CRÉDITOS ---")
    print("Juego desarrollado por: Romero Santiago y Zalazar Nestor")
    print("Materia: Programación I - UTN")
    print("Año: 2025")
    print("Temática: League of Legends")
