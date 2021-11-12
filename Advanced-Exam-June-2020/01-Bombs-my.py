bomb_effects = [int(n) for n in input().split(', ')]
bomb_casings = [int(n) for n in input().split(', ')]


bombs = {
    'Datura Bombs': 40,
    'Cherry Bombs': 60,
    'Smoke Decoy Bombs': 120
}
datura_bombs_n = 0
cherry_bombs_n = 0
smoke_decoy_bombs = 0


while (len(bomb_effects) > 0 and len(bomb_casings) > 0)\
        or (datura_bombs_n >= 3 and cherry_bombs_n >= 3 and smoke_decoy_bombs >= 3):
    if len(bomb_effects) == 0 or len(bomb_casings) == 0:
        break
    if bomb_effects[0] + bomb_casings[-1] == 40:
        datura_bombs_n += 1
        bomb_effects.pop(0)
        bomb_casings.pop()
    elif bomb_effects[0] + bomb_casings[-1] == 60:
        cherry_bombs_n += 1
        bomb_effects.pop(0)
        bomb_casings.pop()
    elif bomb_effects[0] + bomb_casings[-1] == 120:
        smoke_decoy_bombs += 1
        bomb_effects.pop(0)
        bomb_casings.pop()
    else:
        bomb_casings[-1] -= 5
    if datura_bombs_n >= 3 and cherry_bombs_n >= 3 and smoke_decoy_bombs >= 3:
        break

if datura_bombs_n >= 3 and cherry_bombs_n >= 3 and smoke_decoy_bombs >= 3:
    print('Bene! You have successfully filled the bomb pouch!')
else:
    print("You don't have enough materials to fill the bomb pouch.")

if len(bomb_effects) > 0:
    print(f"Bomb Effects: {', '.join([str(x) for x in bomb_effects])}")
else:
    print("Bomb Effects: empty")

if len(bomb_casings) > 0:
    print(f"Bomb Casings: {', '.join([str(x) for x in bomb_casings])}")
else:
    print("Bomb Casings: empty")

print(f'Cherry Bombs: {cherry_bombs_n}')
print(f'Datura Bombs: {datura_bombs_n}')
print(f'Smoke Decoy Bombs: {smoke_decoy_bombs}')
