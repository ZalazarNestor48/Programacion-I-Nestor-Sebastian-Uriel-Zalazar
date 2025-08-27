def calcular_edad(anio_nacimiento):
    anio_actual = 2025   
    return anio_actual - anio_nacimiento

anio = int(input("Ingresa tu año de nacimiento: "))
edad = calcular_edad(anio)

print("Tu edad es:", edad)
