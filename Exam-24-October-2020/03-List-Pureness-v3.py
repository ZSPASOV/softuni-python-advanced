from collections import deque
from sys import maxsize


def best_list_pureness(list_of_numbers, k):
    best_sum = -maxsize
    sum = 0
    rotation = 0
    queue = deque(list_of_numbers)
    for i in range(k):
        for j in range(len(queue)):
            sum += queue[j] * j
        if sum > best_sum:
            best_sum = sum
            rotation = i
        sum = 0
        queue.rotate(1)
    return f'Best pureness {best_sum} after {rotation} rotations'

test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)


test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)

test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
