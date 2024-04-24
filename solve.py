from cube import Cube
import heapq
from random import shuffle

allowed_moves_edges = ['U', 'CU', 'D', 'CD', 'L', 'CL', 'R', 'CR', 'F', 'CF', 'B', 'CB']
layer_edges =  [('U', 'F'), ('U', 'R'), ('U', 'L'), ('U', 'B'), ('D', 'F'), ('D', 'R'), ('D', 'L'), ('D', 'B'), ('F', 'R'), ('F', 'L'), ('B', 'R'), ('B', 'L')]
layer_corners = [('U', 'F', 'R'), ('U', 'R', 'B'), ('U', 'B', 'L'), ('U', 'L', 'F'), ('D', 'F', 'R'), ('D', 'R', 'B'), ('D', 'B', 'L'), ('D', 'L', 'F')]

def is_corner_oriented_correctly(cube : Cube, corner):
    oriented = cube.get_corner_orientations()
    for faces, state in oriented.items():
        if faces == corner:
            if state == 'correct':
                return True
            else:
                return False

def is_edge_oriented_correctly(cube : Cube, edge):
    oriented = cube.get_edge_orientations()
    for faces, state in oriented.items():
        #print(faces, state)   
        if faces == edge:
            if state == 'correct':
                return True
            else:
                return False

def generate_successors(cube : Cube, moves, last_move=None):
    successors = []
    for move in moves:
        if last_move and (move == reverse_move(last_move)):
            continue
        new_cube = cube.copy()
        new_cube.make_move(move)
        successors.append((new_cube, move))
    return successors

def reverse_move(move):
    if move.startswith('C'):  # Assume 'C' stands for counter-clockwise or 'prime'
        return move[1]  # Remove 'C' to get the clockwise movement
    elif '2' in move:
        return move  # A double move (180 degrees) is its own inverse
    else:
        return 'C' + move  # Add 'C' to make it counter-clockwise

def heuristic_combined(cube):
    incorrect_edges = 0
    incorrect_corners = 0
    
    for edge in layer_edges:
        if not is_edge_oriented_correctly(cube, edge):
            incorrect_edges += 1
            
    for corner in layer_corners:
        if not is_corner_oriented_correctly(cube, corner):
            incorrect_corners += 1
            
    return incorrect_edges + incorrect_corners
def solve_combined(cube):
    open_set = []
    heapq.heappush(open_set, (heuristic_combined(cube), 0, cube, []))
    visited = set()

    while open_set:
        current_estimate, current_cost, current_cube, path = heapq.heappop(open_set)

        if heuristic_combined(current_cube) == 0:  
            return path
        
        if current_cube in visited:
            continue
        visited.add(current_cube)

        for successor, move in generate_successors(current_cube, allowed_moves_edges, path[-1] if path else None):
            new_cost = current_cost + 1  
            new_estimate = new_cost + heuristic_combined(successor)
            heapq.heappush(open_set, (new_estimate, new_cost, successor, [move] + path))

    return None


def solve_combined_with_threshold(cube, threshold):
    open_set = []
    heapq.heappush(open_set, (heuristic_combined(cube), 0, cube, []))
    visited = set()

    solutions = []
    while open_set:
        current_estimate, current_cost, current_cube, path = heapq.heappop(open_set)

        if heuristic_combined(current_cube) == 0:  
            solutions.append(path)
            if len(solutions) == threshold:
                break
        
        if current_cube in visited:
            continue
        visited.add(current_cube)

        successors = generate_successors(current_cube, allowed_moves_edges, path[-1] if path else None)
        shuffle(successors) 
        for successor, move in successors:
            new_cost = current_cost + 1
            new_estimate = new_cost + heuristic_combined(successor)
            heapq.heappush(open_set, (new_estimate, new_cost, successor, [move] + path))

    return solutions

""" def heuristic_phase_1(cube):
    incorrect_edges = 0
    for edge in layer_edges:
        if not is_edge_oriented_correctly(cube, edge):
            incorrect_edges += 1
    return incorrect_edges

def heuristic_phase_2(cube):
    incorrect_corners = 0
    for corner in layer_corners:
        if not is_corner_oriented_correctly(cube, corner):
            incorrect_corners += 1
    return incorrect_corners

def solve_phase_1(cube):
    open_set = []
    heapq.heappush(open_set, (heuristic_phase_1(cube), 0, cube, []))
    visited = set()

    while open_set:
        current_estimate, current_cost, current_cube, path = heapq.heappop(open_set)

        if heuristic_phase_1(current_cube) == 0:  
            return path
        
        if current_cube in visited:
            continue
        visited.add(current_cube)

        for successor, move in generate_successors(current_cube, allowed_moves_edges, path[-1] if path else None):
            new_cost = current_cost + 1  
            new_estimate = new_cost + heuristic_phase_1(successor)
            heapq.heappush(open_set, (new_estimate, new_cost, successor, path + [move]))

    return None 

def solve_phase_2(cube):
    open_set = []
    heapq.heappush(open_set, (heuristic_phase_2(cube), 0, cube, []))
    visited = set()

    while open_set:
        current_estimate, current_cost, current_cube, path = heapq.heappop(open_set)

        if heuristic_phase_2(current_cube) == 0:  
            return path
        
        if current_cube in visited:
            continue
        visited.add(current_cube)

        for successor, move in generate_successors(current_cube, allowed_moves_edges, path[-1] if path else None):
            new_cost = current_cost + 1  
            new_estimate = new_cost + heuristic_phase_2(successor)
            heapq.heappush(open_set, (new_estimate, new_cost, successor, path + [move]))

    return None """