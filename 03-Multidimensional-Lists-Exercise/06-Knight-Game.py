def is_valid(pos, size):
    row = pos[0]
    col = pos[1]
    return 0 <= row < size and 0 <= col < size


def get_killed_knights(row, col, size, board):
    killed_knights = 0
    # na 1:31:06 ima primer v excel zashto sa tiq chisla
    # tova sa kolko reda i kolko koloni nazad ili napred trqbva da se
    # dviji konq za da ucelva drugi kone
    rows = [-2, -1, 1, 2, 2, 1, -1, -2]
    cols = [1, 2, 2, 1, -1, -2, -2, -1]
    for i in range(8):
        current_pos = [row + rows[i], col + cols[i]]
        if is_valid(current_pos, size) and board[current_pos[0]][current_pos[1]] == "K":
            killed_knights += 1
    return killed_knights


n = int(input())
board = []
total_kills = 0

for _ in range(n):
    board.append([x for x in input()])

while True:
    most_kills = 0
    to_kill = []

    for row in range(n):
        for col in range(n):
            if board[row][col] == "K":
                killed_knights = get_killed_knights(row, col, n, board)
                if killed_knights > most_kills:
                    most_kills = killed_knights
                    to_kill = [row, col]

    if most_kills == 0:
        break

    to_kill_row = to_kill[0]
    to_kill_col = to_kill[1]
    board[to_kill_row][to_kill_col] = "0"
    total_kills += 1

print(total_kills)


# ot uprajnenia instanciq may 2020
# algoritama e da minavame prez matricata i vseki put da mahame konq koito moje da udari nai mnogo drugi
# sled tova minavame pak
# pravim go dokato stignem moment v koito nikoi kon ne moje da udari drugi
# printvame min kone koito trqbva da se mahnat

# na 1:41:52 pravi debug