from cube import Cube
import solve
if __name__ == "__main__":
    try:
        my_cube = Cube('cuboDes.txt')
        my_cube.print_cube()
    except Exception as e:
        print(e)
    #print(solve.solve_phase_1(my_cube))
    cube = Cube()
    cube.print_cube()
    cube.rotate_face_clockwise('F')
    cube.rotate_face_clockwise('U')
    cube.rotate_face_clockwise('U')
    cube.rotate_face_clockwise('U')
    cube.rotate_face_clockwise('R')
    cube.rotate_face_clockwise('F')
    cube.rotate_face_clockwise('L')
    cube.rotate_face_clockwise('B')
    cube.rotate_face_clockwise('D')
    #cube.rotate_face_clockwise('L')
    #cube.rotate_face_clockwise('R')
    cube.print_cube()
    movimientos = solve.solve_combined(cube)
    movimientos_reverse = movimientos[::-1]
    for movimiento in movimientos_reverse:
        print(movimiento)
        cube.make_move(movimiento)
    cube.print_cube()
    




    """ for movimiento in movimientos:
        my_cube.make_move(movimiento)
    my_cube.print_cube() """
    """ movimientos = solve.solve_combined(cube)
    print(movimientos)
    for movimiento in movimientos:
        my_cube.make_move(movimiento)
    my_cube.print_cube()
 """








    """ my_cube.rotate_face_clockwise('F')
    my_cube.print_cube()
    print(solve.is_edge_oriented_correctly(my_cube, ('F', 'R'))) """


    """ print(lookup_tables.generar_tabla_orientacion_aristas()) """

    """ # Nombre del archivo donde deseas guardar la tabla
    nombre_archivo = 'tabla_orientacion.dat'

    # Llamar a la función para guardar la tabla en el archivo
    lookup_tables.guardar_tabla_en_archivo(tabla_orientacion, nombre_archivo)
 """
    """ cube = Cube()
    cube.print_cube()
    cube.rotate_face_clockwise('F')
    cube.rotate_face_counterclockwise('F')
    cube.print_cube() """

    """ path = my_cube.a_star()
    print(path) 
     # Estado inicial de las aristas donde todas están en la orientación correcta
    initial_orientations = tuple([0] * 12)

    # Lista de movimientos para probar
    moves = ['U', 'D', 'L', 'R', 'F', 'B']

    # Aplicar cada movimiento y mostrar el resultado
    for move in moves:
        result = lookup_tables.apply_move_to_edges(initial_orientations, move)
        print(f"Resultado después del movimiento {move}: {result}")"""
 