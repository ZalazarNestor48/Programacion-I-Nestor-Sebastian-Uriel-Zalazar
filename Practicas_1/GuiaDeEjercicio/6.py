def convertir_minutos(minutos):
    horas = minutos // 60        
    sobrantes = minutos % 60     
    return horas, sobrantes


minutos = int(input("Ingresa la cantidad de minutos: "))

horas, sobrantes = convertir_minutos(m)
print(f"{m} minutos son {h} horas y {s} minutos.")
