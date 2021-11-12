# reshava q v lekciq comprehensions lab sled lekciqta na 2:10 hours
# ne e gotova, trqbva da se opravi oshte malko za da q priznae judge
# tova e koda koito e kachil v pastebin, trqbva da se donapravi

def find_player(matrix):
    for y, row in enumerate(matrix):
        for x, value in enumerate(row):
            if value == 'P':
                return x, y


def find_bunnies(matrix):
    bunnies = []
    for y, row in enumerate(matrix):
        for x, value in enumerate(row):
            if value == 'B':
                bunnies.append((x, y))
    return bunnies


n, m = [int(x) for x in input().split(' ')]
lair = [list(input()) for _ in range(n)]
directions = list(input())
player_x, player_y = find_player(lair)
bunny_multiplication_directions = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0),
]

last_player_x, last_player_y = None, None

won = False
lost = False

for direction in directions:
    lair[player_y][player_x] = '.'
    last_player_x = player_x
    last_player_y = player_y

    if direction == 'U':
        player_y -= 1
    elif direction == 'D':
        player_y += 1
    elif direction == 'L':
        player_x -= 1
    elif direction == 'R':
        player_x += 1

    if player_x < 0 or player_x >= m or player_y >= n or player_y < 0:
        won = True
    else:
        at_position = lair[player_y][player_x]
        if at_position == 'B':
            lost = True
            last_player_x = player_x
            last_player_y = player_y
        else:
            lair[player_y][player_x] = 'P'

    for bunny_x, bunny_y in find_bunnies(lair):
        if lost:
            break
        for delta_x, delta_y in bunny_multiplication_directions:
            new_bunny_x = bunny_x + delta_x
            new_bunny_y = bunny_y + delta_y
            if lost:
                break
            if new_bunny_x >= 0 and new_bunny_x < m and new_bunny_y >= 0 and new_bunny_y < n:
                at_position = lair[new_bunny_y][new_bunny_x]
                lair[new_bunny_y][new_bunny_x] = 'B'
                if at_position == 'P':
                    lost = True
                    break
    # for row in lair:
    #     print(''.join(row))
    # print('====')
    if won:
        break
    if lost:
        break


for row in lair:
    print(''.join(row))

if won:
    print(f'won: {last_player_y} {last_player_x}')

elif lost:
    print(f'dead: {last_player_y} {last_player_x}')
