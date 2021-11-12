import re


with open('words.txt') as words_fh, open('input.txt') as input_fh:
    words = words_fh.read().split()
    text = input_fh.read()


words_occurrences = {}


for word in words:
    matches = re.findall(rf'[\s-]({word})[\s.,?!]', text, re.MULTILINE + re.IGNORECASE)
    words_occurrences[word.lower()] = len(matches)

with open('output.txt', 'w') as output_fh:
    for word, occurences in sorted(words_occurrences.items(), key=lambda t: -t[1]):
        print(f'{word} - {occurences}', file=output_fh)
