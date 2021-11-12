def move(dy, dx):
    global snake_pos, game_over, food_quantity
    y, x = snake_pos
    territory[y][x] = '.'
    new_y = y + dy
    new_x = x + dx
    if new_y > (n - 1) or new_y < 0 or new_x > (n - 1) or new_x < 0:
        game_over = True
        return
    at_pos = territory[new_y][new_x]
    if at_pos == 'B':
        territory[new_y][new_x] = '.'
        new_y, new_x = search_matrix(territory, 'B')
    elif at_pos == '*':
        food_quantity += 1
        if food_quantity >= 10:
            game_over = True
    territory[new_y][new_x] = 'S'
    snake_pos = (new_y, new_x)