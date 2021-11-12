resuling_text = ''
with open('random_text.txt', 'r') as random_file:
    for index, line in enumerate(random_file):
        length= len([element for element in line if element.isalpha()])
        counter = 0
        for element in line:
            if element in "',.!?\";:-":
                counter += 1
        resuling_text += f'line {index + 1}: {line[:-2]} ({length})({counter})\n'

with open('output_random_text.txt', 'w') as file:
    file.write(resuling_text)