def calcular_jugada(dados, categoria):

    # Obtenemos los valores numéricos de los dados
    valores = [d["puntos"] for d in dados]
    conteos = {v: valores.count(v) for v in valores}

    # Pasamos la categoría a minúsculas para que no importe cómo se escriba
    categoria = categoria.lower().strip()

    #generala
    if categoria == "generala":
        if 5 in conteos.values():
            print("¡GENERALA!")
            return 50
        else:
            print("No hiciste Generala. Se suman los puntos normales.")
            return sum(valores)

    #poker
    elif categoria == "poker":
        if 4 in conteos.values():
            print("PÓKER!")
            return 40
        else:
            print("No hiciste Póker. Se suman los puntos normales.")
            return sum(valores)

    #full
    elif categoria == "full":
        if sorted(conteos.values()) == [2, 3]:
            print("FULL!")
            return 30
        else:
            print("No hiciste Full. Se suman los puntos normales.")
            return sum(valores)

    #escalera
    elif categoria == "escalera":
        if sorted(valores) in ([1, 2, 3, 4, 5], [2, 3, 4, 5, 6]):
            print("ESCALERA!")
            return 20
        else:
            print("No hiciste Escalera. Se suman los puntos normales.")
            return sum(valores)

    #categoria desconocida
    else:
        print("Categoría no reconocida. Se suman los puntos normales.")
        return sum(valores)
