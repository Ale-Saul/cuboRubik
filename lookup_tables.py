from collections import deque
import pickle

def apply_move_to_edges(edge_orientations, move):
    # Asigna el índice de cada arista a una variable para mejorar la legibilidad
    UB, UR, UF, UL, DB, DR, DF, DL, FR, FL, BR, BL = range(12)
    
    # Crea una copia de las orientaciones actuales para modificar
    new_orientations = list(edge_orientations)
    
    if move == 'U' or move == 'D':
        # U y D no cambian la orientación, solo permutan
        if move == 'U':
            new_orientations[UB], new_orientations[UR], new_orientations[UF], new_orientations[UL] = \
                edge_orientations[UR], edge_orientations[UF], edge_orientations[UL], edge_orientations[UB]
        if move == 'D':
            new_orientations[DB], new_orientations[DR], new_orientations[DF], new_orientations[DL] = \
                edge_orientations[DR], edge_orientations[DF], edge_orientations[DL], edge_orientations[DB]
    elif move in ['L', 'R', 'F', 'B']:
        # L, R, F, B cambian la orientación de las aristas afectadas
        if move == 'L':
            new_orientations[UL], new_orientations[FL], new_orientations[DL], new_orientations[BL] = \
                edge_orientations[FL] ^ 1, edge_orientations[DL] ^ 1, edge_orientations[BL] ^ 1, edge_orientations[UL] ^ 1
        if move == 'R':
            new_orientations[UR], new_orientations[BR], new_orientations[DR], new_orientations[FR] = \
                edge_orientations[BR] ^ 1, edge_orientations[DR] ^ 1, edge_orientations[FR] ^ 1, edge_orientations[UR] ^ 1
        if move == 'F':
            new_orientations[UF], new_orientations[FR], new_orientations[DF], new_orientations[FL] = \
                edge_orientations[FL] ^ 1, edge_orientations[UF] ^ 1, edge_orientations[FR] ^ 1, edge_orientations[DF] ^ 1
        if move == 'B':
            new_orientations[UB], new_orientations[BR], new_orientations[DB], new_orientations[BL] = \
                edge_orientations[BR] ^ 1, edge_orientations[DB] ^ 1, edge_orientations[BL] ^ 1, edge_orientations[UB] ^ 1

    return tuple(new_orientations)




def generar_tabla_orientacion_aristas():
    moves = ["U", "D", "L", "R", "F", "B"]
    initial_state = tuple([0] * 12)  # 12 aristas, asumiendo orientación inicial correcta
    queue = deque([(initial_state, 0)])  # Estado del cubo y profundidad de movimiento
    seen = {initial_state}
    orientation_table = {}

    while queue:
        current_orientations, depth = queue.popleft()
        for move in moves:
            new_orientations = apply_move_to_edges(current_orientations, move)
            if new_orientations not in seen:
                seen.add(new_orientations)
                queue.append((new_orientations, depth + 1))
                orientation_table[new_orientations] = depth + 1

    return orientation_table

def guardar_tabla_en_archivo(tabla, nombre_archivo):
    with open(nombre_archivo, 'wb') as archivo:
        pickle.dump(tabla, archivo)
        print("Datos guardados:", tabla) 
        
def cargar_tabla_desde_archivo(nombre_archivo):
    with open(nombre_archivo, 'rb') as archivo:
        tabla = pickle.load(archivo)
        print("Datos cargados:", tabla)  # Imprimir los datos después de cargar
        return tabla