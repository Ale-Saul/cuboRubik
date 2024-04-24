from cube import Cube
import solve

def desarmar(cubo : Cube):
    cubo.rotate_face_clockwise('F')
    cubo.rotate_face_clockwise('U')
    cubo.rotate_face_clockwise('U')
    cubo.rotate_face_clockwise('U')
    cubo.rotate_face_clockwise('R')
    cubo.rotate_face_clockwise('F')
    cubo.rotate_face_clockwise('L')
    cubo.rotate_face_clockwise('B')
    cubo.rotate_face_clockwise('D')

def realizar_movimientos(cubo : Cube):
    while True:
        print("1. Mover cara de arriba a la derecha")
        print("2. Mover cara de arriba a la izquierda")
        print("3. Mover cara de abajo a la derecha")
        print("4. Mover cara de abajo a la izquierda")
        print("5. Mover cara de adelante a la derecha")
        print("6. Mover cara de adelante a la izquierda")
        print("7. Mover cara de atrás a la derecha")
        print("8. Mover cara de atrás a la izquierda")
        print("9. Mover cara de la derecha hacia arriba")
        print("10. Mover cara de la derecha hacia abajo")
        print("11. Mover cara de la izquierda hacia arriba")
        print("12. Mover cara de la izquierda hacia abajo")
        print("0. Salir")
        opcion = input("Elige una opción: ")
        if opcion == '1':
            cubo.rotate_face_clockwise('U')
            cubo.print_cube()
        elif opcion == '2':
            cubo.rotate_face_counterclockwise('U')
            cubo.print_cube()
        elif opcion == '3':
            cubo.rotate_face_clockwise('D')
            cubo.print_cube()
        elif opcion == '4':
            cubo.rotate_face_counterclockwise('D')
            cubo.print_cube()
        elif opcion == '5':
            cubo.rotate_face_clockwise('F')
            cubo.print_cube()
        elif opcion == '6':
            cubo.rotate_face_counterclockwise('F')
            cubo.print_cube()
        elif opcion == '7':
            cubo.rotate_face_clockwise('B')
            cubo.print_cube()
        elif opcion == '8':
            cubo.rotate_face_counterclockwise('B')
            cubo.print_cube()
        elif opcion == '9':
            cubo.rotate_face_clockwise('R')
            cubo.print_cube()
        elif opcion == '10':
            cubo.rotate_face_counterclockwise('R')
            cubo.print_cube()
        elif opcion == '11':
            cubo.rotate_face_clockwise('L')
            cubo.print_cube()
        elif opcion == '12':
            cubo.rotate_face_counterclockwise('L')
            cubo.print_cube()
        elif opcion == '0':
            break
        else:
            print("Opción no válida")

def menu():
    cube = Cube()
    while True:
        print("Menú principal")
        print("1. Mostrar cubo")
        print("2. Desarmar cubo predeterminado")
        print("3. Mover cubo")
        print("4. Resolver cubo")
        print("5. Reiniciar cubo")
        print("6. Obtener soluciones suboptimas")
        print("7. Cargar cubo desde archivo")
        print("8. Resolver cubo de archivo")
        print("9. Mostrar Cubo de archivo")
        print("10. Obtener soluciones suboptimas del cubo del archivo")
        print("0. Salir")
        opcion = input("Elige una opción: ")
        if opcion == '1':
            cube.print_cube()
        elif opcion == '2':
            desarmar(cube)
            cube.print_cube()
        elif opcion == '3':
            realizar_movimientos(cube)
            cube.print_cube()
        elif opcion == '4':
            movimientos = solve.solve_combined(cube)
            movimientos_reverse = movimientos[::-1]
            for movimiento in movimientos_reverse:
                print(movimiento)
                cube.make_move(movimiento)
            cube.print_cube()
        elif opcion == '5':
            cube.reset()
            cube.print_cube()
        elif opcion == '6':
            input_threshold = input("Ingresa el numero de soluciones a obtener: ")
            soluciones = solve.solve_combined_with_threshold(cube, int(input_threshold))
            for solucion in soluciones:
                print(solucion)
        elif opcion == '7':
            nombre_archivo = input("Ingresa el nombre del archivo: ")
            try:
                cube_archivo = Cube(nombre_archivo)
                if cube_archivo.is_valid_configuration():
                    print("Cubo cargado correctamente")
                else:
                    print("El cubo no tiene una configuración válida")
                    cube_archivo = None
            except Exception as e:
                print(e)
        elif opcion == '8':
            if not cube_archivo:
                print("Primero carga un cubo desde archivo")
                continue
            else:
                movimientos = solve.solve_combined(cube_archivo)
                movimientos_reverse = movimientos[::-1]
                for movimiento in movimientos_reverse:
                    print(movimiento)
                    cube_archivo.make_move(movimiento)
                cube_archivo.print_cube()
        elif opcion == '9':
            if not cube_archivo:
                print("Primero carga un cubo desde archivo")
                continue
            else:
                cube_archivo.print_cube()
        elif opcion == '10':
            if not cube_archivo:
                print("Primero carga un cubo desde archivo")
                continue
            else:
                input_threshold = input("Ingresa el numero de soluciones a obtener: ")
                soluciones = solve.solve_combined_with_threshold(cube_archivo, int(input_threshold))
                for solucion in soluciones:
                    print(solucion)
        elif opcion == '0':
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    menu()