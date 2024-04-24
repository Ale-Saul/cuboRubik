
class Cube:
    def __init__(self, config=None):
        if config is None:
            self.reset()
        else:
            self.faces = self.load_from_file(config)
        # Definir las relaciones de adyacencia entre las caras del cubo
        self.setup_edge_adjacency()
        self.setup_corner_adjacency()
    
    def __lt__(self, other):
        # Una forma simple podría ser comparar una representación en cadena de los estados del cubo
        # o cualquier otra lógica que defina cuándo un cubo es "menor" que otro
        return str(self.faces) < str(other.faces)

    # Además de __lt__, puedes implementar otros como __eq__ y __gt__ para una comparación completa.
    def __eq__(self, other):
        if not isinstance(other, Cube):
            return NotImplemented
        return str(self.faces) == str(other.faces)

    def __hash__(self):
        state_hash = tuple(tuple(tuple(row) for row in face) for face in self.faces.values())
        return hash(state_hash) 
    
    def setup_edge_adjacency(self):
        self.edge_adjacency = {
            ('U', 'F'): [(2, 1), (0, 1)],
            ('U', 'R'): [(1, 2), (0, 1)],
            ('U', 'B'): [(0, 1), (0, 1)],
            ('U', 'L'): [(1, 0), (0, 1)],
            ('D', 'F'): [(0, 1), (2, 1)],
            ('D', 'R'): [(1, 2), (2, 1)],
            ('D', 'B'): [(2, 1), (2, 1)],
            ('D', 'L'): [(1, 0), (2, 1)],
            ('F', 'R'): [(1, 2), (1, 0)],
            ('F', 'L'): [(1, 0), (1, 2)],
            ('B', 'R'): [(1, 0), (1, 2)],
            ('B', 'L'): [(1, 2), (1, 0)]
        }
    
    def setup_corner_adjacency(self):
        self.corner_adjacency = {
            ('U', 'F', 'R'): [(2, 2), (0, 2), (0, 0)],
            ('U', 'R', 'B'): [(0, 2), (0, 2), (0, 0)],
            ('U', 'B', 'L'): [(0, 0), (0, 2), (0, 0)],
            ('U', 'L', 'F'): [(2, 0), (0, 2), (0, 0)],
            ('D', 'F', 'R'): [(0, 2), (2, 2), (2, 0)],
            ('D', 'R', 'B'): [(2, 2), (2, 2), (2, 0)],
            ('D', 'B', 'L'): [(2, 0), (2, 2), (2, 0)],
            ('D', 'L', 'F'): [(0, 0), (2, 2), (2, 0)]
        }

    def reset(self):
        # Retorna un estado resuelto del cubo sin modificar self.faces
        self.faces ={
            'U': [['W']*3 for _ in range(3)],
            'D': [['Y']*3 for _ in range(3)],
            'F': [['R']*3 for _ in range(3)],
            'B': [['O']*3 for _ in range(3)],
            'L': [['G']*3 for _ in range(3)],
            'R': [['B']*3 for _ in range(3)]
        }

    def get_edge_orientations(self):
        # Define las aristas y qué color debe estar en qué cara para ser "correctamente" orientada
        edges = {
            ('U', 'F'): ('W', 'R', self.faces['U'][2][1], self.faces['F'][0][1]),
            ('U', 'R'): ('W', 'B', self.faces['U'][1][2], self.faces['R'][0][1]),
            ('U', 'L'): ('W', 'G', self.faces['U'][1][0], self.faces['L'][0][1]),
            ('U', 'B'): ('W', 'O', self.faces['U'][0][1], self.faces['B'][0][1]),
            ('D', 'F'): ('Y', 'R', self.faces['D'][0][1], self.faces['F'][2][1]),
            ('D', 'R'): ('Y', 'B', self.faces['D'][1][2], self.faces['R'][2][1]),
            ('D', 'L'): ('Y', 'G', self.faces['D'][1][0], self.faces['L'][2][1]),
            ('D', 'B'): ('Y', 'O', self.faces['D'][2][1], self.faces['B'][2][1]),
            ('F', 'R'): ('R', 'B', self.faces['F'][1][2], self.faces['R'][1][0]),
            ('F', 'L'): ('R', 'G', self.faces['F'][1][0], self.faces['L'][1][2]),
            ('B', 'R'): ('O', 'B', self.faces['B'][1][0], self.faces['R'][1][2]),
            ('B', 'L'): ('O', 'G', self.faces['B'][1][2], self.faces['L'][1][0])
        }
        orientations_edges = {}
        for edge, (expected_color1, expected_color2, color1, color2) in edges.items():
            if color1 == expected_color1 and color2 == expected_color2:
                #print(f"La arista {edge} está orientada correctamente {color1}, {color2}.")
                orientations_edges[edge] = 'correct'
            else:
                #print(f"La arista {edge} está orientada incorrectamente {color1}, {color2}.")
                orientations_edges[edge] = 'incorrect'
        return orientations_edges
        

    def get_corner_orientations(self):
        corners = {
            ('U', 'F', 'R'): ('W', 'R', 'B', self.faces['U'][2][2], self.faces['F'][0][2], self.faces['R'][0][0]),
            ('U', 'R', 'B'): ('W', 'B', 'O', self.faces['U'][0][2], self.faces['R'][0][2], self.faces['B'][0][0]),
            ('U', 'B', 'L'): ('W', 'O', 'G', self.faces['U'][0][0], self.faces['B'][0][2], self.faces['L'][0][0]),
            ('U', 'L', 'F'): ('W', 'G', 'R', self.faces['U'][2][0], self.faces['L'][0][2], self.faces['F'][0][0]),
            ('D', 'F', 'R'): ('Y', 'R', 'B', self.faces['D'][0][2], self.faces['F'][2][2], self.faces['R'][2][0]),
            ('D', 'R', 'B'): ('Y', 'B', 'O', self.faces['D'][2][2], self.faces['R'][2][2], self.faces['B'][2][0]),
            ('D', 'B', 'L'): ('Y', 'O', 'G', self.faces['D'][2][0], self.faces['B'][2][2], self.faces['L'][2][0]),
            ('D', 'L', 'F'): ('Y', 'G', 'R', self.faces['D'][0][0], self.faces['L'][2][2], self.faces['F'][2][0])
        }
        orientations_corners = {}
        for corner, (expected_color1, expected_color2, expected_color3, color1, color2, color3) in corners.items():
            if color1 == expected_color1 and color2 == expected_color2 and color3 == expected_color3:
                #print(f"La esquina {corner} está orientada correctamente {color1}, {color2}, {color3}.")
                orientations_corners[corner] = 'correct'
            else:
                #print(f"La esquina {corner} está orientada incorrectamente {color1}, {color2}, {color3}.")
                orientations_corners[corner] = 'incorrect'
        return orientations_corners

    def get_edge_positions(self):
        # Implementación para obtener la posición de las aristas
        positions_edges = {}
        for (face1, face2), ((row1, col1), (row2, col2)) in self.edge_adjacency.items():
            edge_color_pair = self.faces[face1][row1][col1], self.faces[face2][row2][col2]
            positions_edges[edge_color_pair] = (face1, face2)
        return positions_edges

    def get_corner_positions(self):
        positions_corners = {}
        for (face1, face2, face3), ((row1, col1), (row2, col2), (row3, col3)) in self.corner_adjacency.items():
            corner_color_triplet = self.faces[face1][row1][col1], self.faces[face2][row2][col2], self.faces[face3][row3][col3]
            positions_corners[corner_color_triplet] = (face1, face2, face3)
        return positions_corners

    def rotate_face_clockwise(self, face):
        if face == 'F':
            self.faces['F'] = [list(row) for row in zip(*self.faces['F'][::-1])]
            temp = self.faces['U'][2][:]
            self.faces['U'][2] = [self.faces['L'][2][2], self.faces['L'][1][2], self.faces['L'][0][2]]
            self.faces['L'][2][2], self.faces['L'][1][2], self.faces['L'][0][2] = self.faces['D'][0][::-1]
            self.faces['D'][0] = [self.faces['R'][2][0], self.faces['R'][1][0], self.faces['R'][0][0]]
            self.faces['R'][2][0], self.faces['R'][1][0], self.faces['R'][0][0] = temp[::-1]
        if face == 'B':
            self.faces['B'] = [list(col) for col in reversed(list(zip(*self.faces['B'])))]
            temp = self.faces['U'][0][:]
            self.faces['U'][0] = [self.faces['L'][2][0], self.faces['L'][1][0], self.faces['L'][0][0]]
            self.faces['L'][2][0], self.faces['L'][1][0], self.faces['L'][0][0] = self.faces['D'][2][::-1]
            self.faces['D'][2] = [self.faces['R'][2][2], self.faces['R'][1][2], self.faces['R'][0][2]]
            self.faces['R'][2][2], self.faces['R'][1][2], self.faces['R'][0][2] = temp[::-1]
        if face == 'U':
            self.faces['U'] = [list(col) for col in reversed(list(zip(*self.faces['U'])))]
            temp = self.faces['F'][0][:]
            self.faces['F'][0] = self.faces['L'][0][:]
            self.faces['L'][0] = self.faces['B'][0][:]
            self.faces['B'][0] = self.faces['R'][0][:]
            self.faces['R'][0] = temp
        if face == 'D':
            self.faces['D'] = [list(row) for row in zip(*self.faces['D'][::-1])]
            temp = self.faces['F'][2][:]
            self.faces['F'][2] = self.faces['L'][2][:]
            self.faces['L'][2] = self.faces['B'][2][:]
            self.faces['B'][2] = self.faces['R'][2][:]
            self.faces['R'][2] = temp
        if face == 'L':
            self.faces['L'] = [list(col) for col in reversed(list(zip(*self.faces['L'])))]
            temp = [self.faces['U'][0][0], self.faces['U'][1][0], self.faces['U'][2][0]]
            self.faces['U'][0][0], self.faces['U'][1][0], self.faces['U'][2][0] = self.faces['F'][0][0], self.faces['F'][1][0], self.faces['F'][2][0]
            self.faces['F'][0][0], self.faces['F'][1][0], self.faces['F'][2][0] = self.faces['D'][0][0], self.faces['D'][1][0], self.faces['D'][2][0]
            self.faces['D'][0][0], self.faces['D'][1][0], self.faces['D'][2][0] = self.faces['B'][2][2], self.faces['B'][1][2], self.faces['B'][0][2]
            self.faces['B'][0][2], self.faces['B'][1][2], self.faces['B'][2][2] = temp[2], temp[1], temp[0]
        if face == 'R':
            self.faces['R'] = [list(row) for row in zip(*self.faces['R'][::-1])]
            temp = [self.faces['U'][0][2], self.faces['U'][1][2], self.faces['U'][2][2]]
            self.faces['U'][0][2], self.faces['U'][1][2], self.faces['U'][2][2] = self.faces['F'][0][2], self.faces['F'][1][2], self.faces['F'][2][2]
            self.faces['F'][0][2], self.faces['F'][1][2], self.faces['F'][2][2] = self.faces['D'][0][2], self.faces['D'][1][2], self.faces['D'][2][2]
            self.faces['D'][0][2], self.faces['D'][1][2], self.faces['D'][2][2] = self.faces['B'][2][0], self.faces['B'][1][0], self.faces['B'][0][0]
            self.faces['B'][0][0], self.faces['B'][1][0], self.faces['B'][2][0] = temp[2], temp[1], temp[0]
                
    def rotate_face_counterclockwise(self, face):
        if face == 'F':
            self.faces['F'] = [list(row) for row in reversed(list(zip(*self.faces['F'])))]
            temp = self.faces['U'][2][:]
            self.faces['U'][2] = [self.faces['R'][0][0], self.faces['R'][1][0], self.faces['R'][2][0]]
            self.faces['R'][0][0], self.faces['R'][1][0], self.faces['R'][2][0] = self.faces['D'][0][::-1]
            self.faces['D'][0] = [self.faces['L'][0][2], self.faces['L'][1][2], self.faces['L'][2][2]]
            self.faces['L'][2][2], self.faces['L'][1][2], self.faces['L'][0][2] = temp
        if face == 'B':
            self.faces['B'] = [list(col) for col in zip(*reversed(self.faces['B']))]
            temp = self.faces['U'][0][:]
            self.faces['U'][0] = [self.faces['R'][0][2], self.faces['R'][1][2], self.faces['R'][2][2]]
            self.faces['R'][0][2], self.faces['R'][1][2], self.faces['R'][2][2] = self.faces['D'][2][::-1]
            self.faces['D'][2] = [self.faces['L'][0][0], self.faces['L'][1][0], self.faces['L'][2][0]]
            self.faces['L'][2][0], self.faces['L'][1][0], self.faces['L'][0][0] = temp
        if face == 'U':
            self.faces['U'] = [list(col) for col in zip(*reversed(self.faces['U']))]
            temp = self.faces['F'][0][:]
            self.faces['F'][0] = self.faces['R'][0][:]
            self.faces['R'][0] = self.faces['B'][0][:]
            self.faces['B'][0] = self.faces['L'][0][:]
            self.faces['L'][0] = temp
        if face == 'D':
            self.faces['D'] = [list(row) for row in reversed(list(zip(*self.faces['D'])))]
            temp = self.faces['F'][2][:]
            self.faces['F'][2] = self.faces['R'][2][:]
            self.faces['R'][2] = self.faces['B'][2][:]
            self.faces['B'][2] = self.faces['L'][2][:]
            self.faces['L'][2] = temp

        if face == 'L':
            self.faces['L'] = [list(col) for col in zip(*reversed(self.faces['L']))]
            temp = [self.faces['U'][0][0], self.faces['U'][1][0], self.faces['U'][2][0]]
            self.faces['U'][0][0], self.faces['U'][1][0], self.faces['U'][2][0] = self.faces['B'][2][2], self.faces['B'][1][2], self.faces['B'][0][2]
            self.faces['B'][0][2], self.faces['B'][1][2], self.faces['B'][2][2] = self.faces['D'][2][0], self.faces['D'][1][0], self.faces['D'][0][0]
            self.faces['D'][0][0], self.faces['D'][1][0], self.faces['D'][2][0] = self.faces['F'][0][0], self.faces['F'][1][0], self.faces['F'][2][0]
            self.faces['F'][0][0], self.faces['F'][1][0], self.faces['F'][2][0] = temp[0], temp[1], temp[2]

        if face == 'R':
            self.faces['R'] = [list(row) for row in reversed(list(zip(*self.faces['R'])))]
            temp = [self.faces['U'][0][2], self.faces['U'][1][2], self.faces['U'][2][2]]
            self.faces['U'][0][2], self.faces['U'][1][2], self.faces['U'][2][2] = self.faces['B'][2][0], self.faces['B'][1][0], self.faces['B'][0][0]
            self.faces['B'][0][0], self.faces['B'][1][0], self.faces['B'][2][0] = self.faces['D'][2][2], self.faces['D'][1][2], self.faces['D'][0][2]
            self.faces['D'][0][2], self.faces['D'][1][2], self.faces['D'][2][2] = self.faces['F'][0][2], self.faces['F'][1][2], self.faces['F'][2][2]
            self.faces['F'][0][2], self.faces['F'][1][2], self.faces['F'][2][2] = temp[0], temp[1], temp[2]

    def make_move(self, move):
        if move == 'U':
            self.rotate_face_clockwise('U')
        elif move == 'CU':
            self.rotate_face_counterclockwise('U')
        elif move == 'U2':
            self.rotate_face_clockwise('U')
            self.rotate_face_clockwise('U')
        elif move == 'D':
            self.rotate_face_clockwise('D')
        elif move == 'CD':
            self.rotate_face_counterclockwise('D')
        elif move == 'D2':
            self.rotate_face_clockwise('D')
            self.rotate_face_clockwise('D')
        elif move == 'F':
            self.rotate_face_clockwise('F')
        elif move == 'CF':
            self.rotate_face_counterclockwise('F')
        elif move == 'B':
            self.rotate_face_clockwise('B')
        elif move == 'CB':
            self.rotate_face_counterclockwise('B')
        elif move == 'L':
            self.rotate_face_clockwise('L')
        elif move == 'CL':
            self.rotate_face_counterclockwise('L')
        elif move == 'R':
            self.rotate_face_clockwise('R')
        elif move == 'CR':
            self.rotate_face_counterclockwise('R')
        else:
            raise ValueError(f"El movimiento {move} no es válido.")
        return self

    def copy(self):
        new_cube = Cube()
        new_cube.faces = {face: [row[:] for row in self.faces[face]] for face in self.faces}
        return new_cube

    def load_from_file(self, file_path):
        new_faces = {}
        face_order = ['U', 'D', 'F', 'B', 'L', 'R']
        try:
            with open(file_path, 'r') as file:
                lines = [line.strip() for line in file if line.strip()]
                if len(lines) != 18:
                    raise ValueError("El archivo debe contener exactamente 18 líneas de datos.")
                for i, face in enumerate(face_order):
                    face_lines = lines[i*3:(i+1)*3]
                    new_faces[face] = [list(line) for line in face_lines if len(line) == 3]
                    if any(len(row) != 3 for row in new_faces[face]):
                        raise ValueError("Cada línea debe contener exactamente tres caracteres.")
        except FileNotFoundError:
            raise FileNotFoundError("El archivo especificado no existe.")
        except Exception as e:
            raise Exception(f"Error al cargar el archivo: {e}")
        return new_faces

    def print_cube(self):
        # Usar color_map si desea color en la terminal que soporte ANSI
        color_map = {
            'W': '\033[97mW\033[0m',  # Blanco
            'Y': '\033[93mY\033[0m',  # Amarillo
            'R': '\033[91mR\033[0m',  # Rojos
            'O': '\033[95mO\033[0m',  # Magenta (Naranja)
            'G': '\033[92mG\033[0m',  # Verde
            'B': '\033[94mB\033[0m'   # Azul
        }
        # Construir la representación 2D
        u = '\n'.join('      ' + ' '.join(color_map[x] for x in row) for row in self.faces['U'])
        d = '\n'.join('      ' + ' '.join(color_map[x] for x in row) for row in self.faces['D'])
        f = '\n'.join(' '.join(color_map[x] for x in row) for row in self.faces['F'])
        b = '\n'.join(' '.join(color_map[x] for x in row) for row in self.faces['B'])
        l = '\n'.join(' '.join(color_map[x] for x in row) for row in self.faces['L'])
        r = '\n'.join(' '.join(color_map[x] for x in row) for row in self.faces['R'])
        
        # Alineando las caras en la visualización
        middle = '\n'.join(' '.join(row) for row in zip(l.split('\n'), f.split('\n'), r.split('\n'), b.split('\n')))
        print(f"{u}\n{middle}\n{d}")
        print()

    def is_valid_configuration(self):
        # Contar apariciones de cada color
        color_count = {}
        for face in self.faces:
            for row in self.faces[face]:
                for color in row:
                    color_count[color] = color_count.get(color, 0) + 1

        # Validación de la cantidad de colores
        if any(count != 9 for count in color_count.values()):
            print("Error: Cada color debe aparecer exactamente 9 veces.")
            return False

        # Validación de los centros de cada cara
        expected_centers = {'U': 'W', 'D': 'Y', 'F': 'R', 'B': 'O', 'L': 'G', 'R': 'B'}
        for face, center_color in expected_centers.items():
            if self.faces[face][1][1] != center_color:
                print(f"Error: El centro de la cara {face} debe ser {center_color}.")
                return False

        return True
    
    def is_solved(self):
        # Comprobar que cada cara del cubo tiene un único color y que es el correcto
        expected_centers = {'U': 'W', 'D': 'Y', 'F': 'R', 'B': 'O', 'L': 'G', 'R': 'B'}
        for face, expected_color in expected_centers.items():
            if any(color != expected_color for row in self.faces[face] for color in row):
                return False
        return True
    
"""  def find_edge_position(self, edge_color_pair):
        for (face1, face2), ((row1, col1), (row2, col2)) in self.adjacency.items():
            if (self.faces[face1][row1][col1], self.faces[face2][row2][col2]) == edge_color_pair:
                return face1, (row1, col1)
            if (self.faces[face2][row2][col2], self.faces[face1][row1][col1]) == edge_color_pair:
                return face2, (row2, col2)
        return None
    
    def calculate_moves_for_edge(current_position, target_position):
        face, (row, col) = current_position
        target_face, (target_row, target_col) = target_position
        moves = []
        while (face, (row, col)) != target_position:
            if face == target_face:
                if row < target_row:
                    moves.append('D')
                    face = 'D'
                elif row > target_row:
                    moves.append('U')
                    face = 'U'
                elif col < target_col:
                    moves.append('R')
                    face = 'R'
                elif col > target_col:
                    moves.append('L')
                    face = 'L'
            elif face == 'U':
                if row == 0:
                    moves.append('D')
                    face = 'D'
                elif row == 2:
                    moves.append('U')
                    face = 'U'
                else:
                    moves.append('F')
                    face = 'F'
            elif face == 'D':
                if row == 0:
                    moves.append('U')
                    face = 'U'
                elif row == 2:
                    moves.append('D')
                    face = 'D'
                else:
                    moves.append('F')
                    face = 'F'
            elif face == 'F':
                if col == 0:
                    moves.append('R')
                    face = 'R'
                elif col == 2:
                    moves.append('L')
                    face = 'L'
                else:
                    moves.append('F')
                    face = 'F'
            elif face == 'B':
                if col == 0:
                    moves.append('L')
                    face = 'L'
                elif col == 2:
                    moves.append('R')
                    face = 'R'
                else:
                    moves.append('B')
                    face = 'B'
            elif face == 'L':
                if row == 0:
                    moves.append('U')
                    face = 'U'
                elif row == 2:
                    moves.append('D')
                    face = 'D'
                else:
                    moves.append('L')
                    face = 'L'
            elif face == 'R':
                if row == 0:
                    moves.append('U')
                    face = 'U'
                elif row == 2:
                    moves.append('D')
                    face = 'D'
                else:
                    moves.append('R')
                    face = 'R'
        return moves
    
    def edges_needed_for_cross_on_face(face):
        edges = {
            'U': [('W', 'R'), ('W', 'O'), ('W', 'G'), ('W', 'B')],
            'D': [('Y', 'R'), ('Y', 'O'), ('Y', 'G'), ('Y', 'B')],
            'F': [('R', 'G'), ('R', 'B'), ('O', 'G'), ('O', 'B')],
            'B': [('R', 'G'), ('R', 'B'), ('O', 'G'), ('O', 'B')],
            'L': [('W', 'G'), ('W', 'B'), ('Y', 'G'), ('Y', 'B')],
            'R': [('W', 'G'), ('W', 'B'), ('Y', 'G'), ('Y', 'B')]
        }
        return edges[face]
    
     def solved(self):
        return {
            'U': [['W']*3 for _ in range(3)],
            'D': [['Y']*3 for _ in range(3)],
            'F': [['R']*3 for _ in range(3)],
            'B': [['O']*3 for _ in range(3)],
            'L': [['G']*3 for _ in range(3)],
            'R': [['B']*3 for _ in range(3)]
        }    
    
    def get_target_position(face, edge):
        target_positions = {
            'U': {('W', 'R'): (0, 1), ('W', 'B'): (0, 1), ('W', 'G'): (0, 1), ('W', 'O'): (0, 1)},
            'D': {('Y', 'R'): (0, 1), ('Y', 'B'): (0, 1), ('Y', 'G'): (0, 1), ('Y', 'O'): (0, 1)},
            'F': {('R', 'G'): (0, 1), ('R', 'B'): (0, 2), ('O', 'G'): (0, 0), ('O', 'B'): (0, 1)},
            'B': {('R', 'G'): (0, 1), ('R', 'B'): (0, 2), ('O', 'G'): (0, 0), ('O', 'B'): (0, 1)},
            'L': {('W', 'G'): (0, 1), ('W', 'B'): (0, 0), ('Y', 'G'): (0, 2), ('Y', 'B'): (0, 1)},
            'R': {('W', 'G'): (0, 1), ('W', 'B'): (0, 2), ('Y', 'G'): (0, 0), ('Y', 'B'): (0, 1)}
        }
        return target_positions[face][edge]
 
    def heuristic(self, state):
        # Aquí, 'state' es un diccionario de las caras del cubo con sus colores actuales
        mismatch = 0
        # Suponiendo que self.reset() define cómo debería verse un cubo resuelto
        solved_state = self.solved()
        for face in state:
            for i in range(3):
                for j in range(3):
                    if state[face][i][j] != solved_state[face][i][j]:
                        mismatch += 1
        return mismatch

    def get_successors(self, state):
        moves = ['U', 'D', 'F', 'B', 'L', 'R']
        successors = []
        for move in moves:
            new_state = deepcopy(state)  # Crea una copia del estado dado
            self.rotate_face_clockwise(move)  # Asegúrate de que esto modifica new_state correctamente
            successors.append((new_state, move, 1))
        return successors
  
    def a_star(self):
        open_set = []
        start = (self.heuristic(self.faces), deepcopy(self.faces), [])
        heapq.heappush(open_set, start)
        while open_set:
            current_heuristic, current_state, path = heapq.heappop(open_set)
            
            if self.heuristic(current_state) == 0:  # Cubo está resuelto
                return path
            
            for successor, move, cost in self.get_successors(current_state):
                new_path = path + [move]
                new_cost = len(new_path)  # Todos los movimientos tienen el mismo costo
                heapq.heappush(open_set, (new_cost + self.heuristic(successor), successor, new_path))
        
        return None """