def print_triangle(n):
    for row in range(1, n + 2):
        print(*[i for i in range(1, row)]) # * podava vseki element na lista kato pozicionen argument na print()
    for row in range(n, 0, -1):
        print(*[i for i in range(1, row)])
