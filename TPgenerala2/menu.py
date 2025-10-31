from juego import jugar
from archivos import mostrar_estadisticas, mostrar_creditos

def menu_principal():
    while True:
        print("\n=== GENERALA TEMÁTICA - LEAGUE OF LEGENDS ===")
        print("1. Jugar")
        print("2. Estadísticas")
        print("3. Créditos")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            jugar()
        elif opcion == "2":
            mostrar_estadisticas()
        elif opcion == "3":
            mostrar_creditos()
        elif opcion == "4":
            print("¡Gracias por jugar!")
            break
        else:
            print("Opción inválida, intente nuevamente.")