from collections import defaultdict
text = input()

# defaultdict(int) creates an empty dictionary with default values 0
symbols = defaultdict(int)

for symbol in text:
    symbols[symbol] += 1


sorted_dict = dict(sorted(symbols.items(), key=lambda x: x[0]))

for key, value in sorted_dict.items():
    print(f'{key}: {value} time/s')
