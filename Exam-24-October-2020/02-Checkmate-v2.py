# 100 / 100

def is_valid(number, size):
    return 0 <= number < size


n = 8

king_pos = []
queen_positions = []
directions = {'up': (-1, 0), 'right': (0, 1), 'down': (1, 0), 'left': (0, -1),
              'upleft': (-1, -1), 'upright': (-1, 1), 'downleft': (1, -1), 'downright': (1, 1)}
matrix = []
hit_by_queens = 0
killer_queens = []

for row in range(n):
    line = [i for i in list(input()) if i != ' ']
    if 'K' in line:
        king_pos = [row, line.index('K')]
    matrix.append(line)

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == 'Q':
            queen_positions.append((i, j))


for direction in directions:

    row = king_pos[0]
    col = king_pos[1]

    row_changes = directions[direction][0]
    col_changes = directions[direction][1]

    if not is_valid(row + row_changes, n) or not is_valid(col + col_changes, n):
        continue

    while is_valid(row, n) and is_valid(col, n):
        current_cell = matrix[row][col]
        if current_cell == 'Q':
            hit_by_queens += 1
            killer_queens.append([row, col])
            break
        row += row_changes
        col += col_changes


if hit_by_queens == 0:
    print('The king is safe!')
else:
    for i in killer_queens:
        print(i)