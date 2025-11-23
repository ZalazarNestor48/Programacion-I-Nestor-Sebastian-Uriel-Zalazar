import random
from datos import cartas
from puntuacion import calcular_jugada
from archivos import guardar_puntaje

def tirar_dados():
    return [random.choice(cartas).copy() for _ in range(5)]

def tirar_dados_segun_guardados(dados, guardados):
    nuevos = []
    for i in range(5):
        if guardados[i]:
            nuevos.append(dados[i])
        else:
            nuevos.append(random.choice(cartas).copy())
    return nuevos

def verificar_categoria_valida(dados, categoria):
    valores = [d['puntos'] for d in dados]
    conteos = [valores.count(v) for v in set(valores)]
    cat = categoria.lower()
    if cat == 'generala':
        return 5 in conteos
    if cat in ('poker','póker'):
        return max(conteos) >= 4
    if cat == 'full':
        return sorted(conteos) == [2,3]
    if cat == 'escalera':
        return sorted(valores) in ([1,2,3,4,5],[2,3,4,5,6])
    if cat.endswith('s') and cat[:-1].isdigit():
        return True
    return False

def puntuar(dados, categoria):
    base = calcular_jugada(dados, categoria)
    if not verificar_categoria_valida(dados, categoria):
        if categoria.lower() in ['generala','poker','póker','full','escalera']:
            return 0
    return base

def jugar_consola():
    # conserva modo consola si querés probar en terminal (usa inputs)
    print('Modo consola habilitado (usa inputs).')
    nombre = input('Ingrese su nombre: ').strip() or 'Jugador'
    puntos_totales = 0
    categorias = ['Generala','Póker','Full','Escalera','1s','2s','3s','4s','5s','6s']
    planilla = {c: None for c in categorias}
    turno = 0
    while turno < 10:
        print(f"\\n--- Turno {turno+1} ---")
        dados = tirar_dados()
        print('Dados:', [(d['nombre'], d['puntos']) for d in dados])
        for t in range(2):
            respuesta = input('Ingrese los números de los dados que quiere mantener (ej: 1,3) o ENTER para tirar todos: ').strip()
            if respuesta == '':
                for i in range(5):
                    dados[i] = random.choice(cartas)
            else:
                mantener = [x.strip() for x in respuesta.split(',') if x.strip().isdigit()]
                for i in range(5):
                    if str(i+1) not in mantener:
                        dados[i] = random.choice(cartas)
            print('Dados:', [(d['nombre'], d['puntos']) for d in dados])
        disponible = [c for c in categorias if planilla[c] is None]
        print('Categorias disponibles:', ', '.join(disponible))
        cat = input('Ingrese la categoría donde desea anotar el puntaje: ').strip()
        while cat not in categorias or planilla.get(cat) is not None:
            cat = input('Categoría inválida o ya usada. Reingrese: ').strip()
        puntos = puntuar(dados, cat)
        planilla[cat] = puntos
        puntos_totales += puntos
        turno += 1
    print('Fin. Puntaje:', puntos_totales)
    guardar_puntaje(nombre, puntos_totales)