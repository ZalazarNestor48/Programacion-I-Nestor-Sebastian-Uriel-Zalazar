def calcular_jugada(dados, categoria):
    # Ejemplo básico: calcular Generala, Poker, Full, Escalera
    valores = [d["puntos"] for d in dados]
    conteos = {v: valores.count(v) for v in valores}

    if 5 in conteos.values():
        print("¡GENERALA!")
        return 50
    elif 4 in conteos.values():
        print("PÓKER")
        return 40
    elif sorted(valores) in ([1,2,3,4,5], [2,3,4,5,6]):
        print("ESCALERA")
        return 20
    elif sorted(conteos.values()) == [2,3]:
        print("FULL")
        return 30
    else:
        return sum(valores)
