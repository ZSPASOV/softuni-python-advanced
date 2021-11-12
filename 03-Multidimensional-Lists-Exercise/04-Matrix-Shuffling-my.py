rows, cols = [int(n) for n in input().split()]

matrix = []
for i in range(rows):
    row =  input().split(' ')
    matrix.append([])
    for j in range(cols):
       matrix[i].append(row[j])


command = input()
while command != 'END':
    args = command.split()
    try:
        action = args[0]
        row1 = int(args[1])
        col1 = int(args[2])
        row2 = int(args[3])
        col2 = int(args[4])
        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
        for row_for_print in matrix:
            print(" ".join([str(i) for i in row_for_print]))
        command = input()
    except IndexError or action != 'swap':
        print("Invalid input!")
        command = input()
