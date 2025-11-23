def calcular_jugada(dados, categoria):
    valores = [d['puntos'] for d in dados]
    conteos = {v: valores.count(v) for v in set(valores)}
    categoria = categoria.lower().strip()

    if categoria == 'generala':
        if 5 in conteos.values():
            return 50
        else:
            return sum(valores)

    elif categoria == 'poker' or categoria == 'póker':
        if 4 in conteos.values():
            return 40
        else:
            return sum(valores)

    elif categoria == 'full':
        if sorted(conteos.values()) == [2, 3]:
            return 30
        else:
            return sum(valores)

    elif categoria == 'escalera':
        if sorted(valores) in ([1,2,3,4,5],[2,3,4,5,6]):
            return 20
        else:
            return sum(valores)

    for i in range(1,7):
        key = f"{i}s"
        if categoria == key:
            return valores.count(i) * i

    return sum(valores)