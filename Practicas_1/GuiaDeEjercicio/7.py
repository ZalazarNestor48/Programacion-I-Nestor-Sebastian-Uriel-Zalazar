def verificar_acceso(edad):
    return edad >= 18

edad = int(input("Ingresa tu edad: "))

if verificar_acceso(edad):
    print("Acceso permitido. Eres mayor de edad.")
else:
    print("Acceso denegado. Eres menor de edad.")
