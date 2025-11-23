import csv
import os

PUNTAJES_CSV = 'puntajes.csv'

def guardar_puntaje(nombre: str, puntos: int, archivo: str = PUNTAJES_CSV) -> None:
    existe = os.path.exists(archivo)
    modo = 'a' if existe else 'w'
    with open(archivo, modo, newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        if not existe:
            writer.writerow(['nombre','puntaje'])
        writer.writerow([nombre, puntos])

def leer_puntajes_csv(archivo: str = PUNTAJES_CSV) -> list:
    if not os.path.exists(archivo):
        return []
    with open(archivo, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        resultados = []
        for row in reader:
            try:
                resultados.append((row['nombre'], int(row['puntaje'])))
            except Exception:
                continue
    resultados.sort(key=lambda x: x[1], reverse=True)
    return resultados

def top_n(n: int = 10, archivo: str = PUNTAJES_CSV) -> list:
    return leer_puntajes_csv(archivo)[:n]