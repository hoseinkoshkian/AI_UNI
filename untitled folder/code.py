import random

def print_board(board):
    for row in board:
        print(" ".join("Q" if col == 1 else "." for col in row))
    print("\n")

def create_initial_board(n):
    board = [[0] * n for _ in range(n)]
    for col in range(n):
        row = random.randint(0, n - 1)
        board[row][col] = 1
    return board

def calculate_conflicts(board):
    n = len(board)
    conflicts = 0

    for col in range(n):
        row = [i for i in range(n) if board[i][col] == 1][0]

   
        for other_col in range(col + 1, n):
            other_row = [i for i in range(n) if board[i][other_col] == 1][0]
            if other_row == row:
                conflicts += 1
       
            if abs(row - other_row) == abs(col - other_col):
                conflicts += 1

    return conflicts

def get_neighbors(board):
    n = len(board)
    neighbors = []

    for col in range(n):
        row = [i for i in range(n) if board[i][col] == 1][0]
        for new_row in range(n):
            if new_row != row:
                neighbor = [row[:] for row in board]
                neighbor[row][col] = 0
                neighbor[new_row][col] = 1
                neighbors.append(neighbor)

    return neighbors

def hill_climbing(board):
    current_board = board
    current_conflicts = calculate_conflicts(current_board)

    while True:
        neighbors = get_neighbors(current_board)
        neighbors_conflicts = [calculate_conflicts(neighbor) for neighbor in neighbors]

        min_conflicts = min(neighbors_conflicts)
        if min_conflicts >= current_conflicts:
            break

     
        current_board = neighbors[neighbors_conflicts.index(min_conflicts)]
        current_conflicts = min_conflicts

    return current_board, current_conflicts

def solve_n_queens(n):
    while True:
        initial_board = create_initial_board(n)
        final_board, conflicts = hill_climbing(initial_board)

        if conflicts == 0:
            return final_board


n = 8
solution = solve_n_queens(n)
print_board(solution)
