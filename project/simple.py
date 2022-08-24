# Game: Connect Four
# ---------------------------------------------------------------------


# Functions
# ---
def accept_matrix_rows_and_columns():
    print("Select rows and columns of the matrix, separated by ', ': ")
    try:
        rows, columns = [int(i) for i in input().split(', ')]
        print(f"You have selected matrix size: {rows}, {columns}")

        create_matrix_with_given_params(rows, columns)
        print_matrix(matrix)

    except ValueError:
        print("---Input must two integers separated by ', '!---\n")
        accept_matrix_rows_and_columns()


def create_matrix_with_given_params(r, c):
    for row in range(r):
        current_row = [0 for c in range(c)]
        matrix.append(current_row)


def print_matrix(m):
    for i in range(len(m)):
        print(m[i])
    print()


def rotate_player_order(p):
    if p == 1:
        p = 2
        return p
    return 1


def move_placement(c):
    for row in range(len(matrix)-1, -1, -1):
        if matrix[row][c-1] == 0:
            matrix[row][c-1] = current_player
            return True
    return False


def win_condition(player, cel_column):
    cell_r = 0
    cell_c = cel_column - 1
    for row in range(len(matrix)):
        if matrix[row][cell_c] == player:
            cell_r = row
            break

    def is_win_condition_in_direction(row, column, direction):
        row_delta, column_delta = direction
        rows_boundary = min(len(matrix), row + 4 * row_delta)
        columns_boundary = min(len(matrix[0]), column + 4 * column_delta)

        counter = 0
        is_row_included = rows_boundary == row
        is_column_included = columns_boundary == column

        while (row < rows_boundary or is_row_included) \
                and (column < columns_boundary or is_column_included) \
                and player == matrix[row][column]:
            counter += 1
            row += row_delta
            column += column_delta

        return counter == 4

    horizontal_deltas = (0, 1)
    vertical_deltas = (1, 0)
    main_diagonal_deltas = (1, 1)
    secondary_diagonal_deltas = (-1, 1)

    return is_win_condition_in_direction(cell_r, cell_c, horizontal_deltas) \
           or is_win_condition_in_direction(cell_r, cell_c, vertical_deltas) \
           or is_win_condition_in_direction(cell_r, cell_c, main_diagonal_deltas) \
           or is_win_condition_in_direction(cell_r, cell_c, secondary_diagonal_deltas)


# Execution
# ---
matrix = []
current_player = 1
reset_symbols = ['R', 'r']

accept_matrix_rows_and_columns()

while 1:
    if not matrix:
        accept_matrix_rows_and_columns()
        continue

    selected_column = input(f"Player {current_player}, please choose a column: \n")

    if selected_column in reset_symbols:
        print("--You have selected to reset!--\n")
        matrix = []
        current_player = 1
        continue

    try:
        selected_column = int(selected_column)
    except ValueError:
        print(f"Selected column must be int!\n")
        continue

    if int(selected_column) > len(matrix[0]):
        print(f"Selected column must be inside matrix!\n")
        continue

    print(f"Selected column: {selected_column}")

    if not move_placement(selected_column):
        print(f"Column already full!\n")
        continue

    print_matrix(matrix)

    if win_condition(current_player, selected_column):
        print("Won")
        break

    current_player = rotate_player_order(current_player)
    print(f"Player changed to: {current_player}\n")




















































