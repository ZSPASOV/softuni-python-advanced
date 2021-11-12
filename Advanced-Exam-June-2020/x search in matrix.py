n = int(input())
territory = [list(input()) for _ in range(n)]


def search_matrix(matrix, search):
    for y, row in enumerate(matrix):
        for x, char in enumerate(row):
            if char == search:
                return y, x


snake_pos = search_matrix(territory, 'S')
print(snake_pos)