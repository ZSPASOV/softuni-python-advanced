n = int(input())
max_length = 0
max_intersection = []
for _ in range(n):
    pair_of_ranges = input().split('-')
    ranges_for_set_a = [int(n) for n in pair_of_ranges[0].split(',')]
    ranges_for_set_b = [int(n) for n in pair_of_ranges[1].split(',')]

    set_a = set(range(ranges_for_set_a[0], ranges_for_set_a[1] + 1))
    set_b = set(range(ranges_for_set_b[0], ranges_for_set_b[1] + 1))
    intesection = set_a & set_b
    if len(intesection) > max_length:
        max_length = len(intesection)
        max_intersection = list(intesection)

print(f'Longest intersection is {max_intersection} with length {max_length}')
