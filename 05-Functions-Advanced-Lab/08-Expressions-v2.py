import itertools

numbers = [n for n in input().split(', ')]
n = len(numbers)
permutations = itertools.product('-+', repeat=n)


for permutation in permutations:
    zipped = list(zip(permutation, numbers))
    expr = ''.join(itertools.chain(*zipped))
    nums = map(lambda z: int(z[1]) if z[0] == '+' else -int(z[1]), zipped)
    res = sum(nums)
    print(f'{expr}={res}')