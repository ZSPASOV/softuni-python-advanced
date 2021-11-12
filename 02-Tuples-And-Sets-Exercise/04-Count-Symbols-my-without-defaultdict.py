text = input()

# defaultdict(int) creates an empty dictionary with default values 0
symbols = {}

for symbol in text:
    if symbol not in symbols:
        symbols[symbol] = 0
    symbols[symbol] += 1

sorted_dict = dict(sorted(symbols.items(), key=lambda x: x[0]))

for key, value in sorted_dict.items():
    print(f'{key}: {value} time/s')
