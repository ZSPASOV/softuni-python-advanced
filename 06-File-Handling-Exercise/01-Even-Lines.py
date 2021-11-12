with open('random_text.txt', 'r') as random_file:
    for index, line in enumerate(random_file):
        if index % 2 == 0:
            for element in '-,.!?':
                line = line.replace(element, '@')
            words = reversed(line.split())
            print(' '.join(words))