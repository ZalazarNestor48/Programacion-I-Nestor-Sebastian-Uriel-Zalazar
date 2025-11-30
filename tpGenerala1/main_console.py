from archivos import top_n
from juego import jugar_consola

def mostrar_creditos():
    print('\\n--- Créditos ---')
    print('Trabajo Práctico: Generala Temática')
    print('Autor: Nestor Zalazar / Romero Santiago')
    print('Materia: Programación I')
    print('-----------------\\n')

def mostrar_estadisticas():
    top = top_n(10)
    print('\\n--- TOP 10 PUNTAJES ---')
    if not top:
        print('No hay puntajes aún.')
    for i,(n,p) in enumerate(top, start=1):
        print(f"{i}. {n} - {p}")
    print('-----------------------\\n')

def main():
    opcion = ''
    while opcion != '4':
        print('\\n==== Generala Temática ====')
        print('1. Jugar (Consola)')
        print('2. Estadísticas')
        print('3. Créditos')
        print('4. Salir')
        opcion = input('Ingrese opción: ').strip()
        if opcion == '1':
            jugar_consola()
        elif opcion == '2':
            mostrar_estadisticas()
        elif opcion == '3':
            mostrar_creditos()
        elif opcion == '4':
            print('Saliendo...')
        else:
            print('Opción inválida')

if __name__ == '__main__':
    main()