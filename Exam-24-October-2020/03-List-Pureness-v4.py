# 100 / 100
from collections import deque

def best_list_pureness(list_of_numbers, k):
    best_sum = 0
    sum = 0
    rotation = 0
    queue = deque(list_of_numbers)
    original_sum = 0
    for index in range(len(queue)):
        original_sum += queue[index] * index
    for i in range(k):
        queue.rotate(1)
        for j in range(len(queue)):
            sum += queue[j] * j
        if sum > best_sum:
            best_sum = sum
            rotation = i
        sum = 0
    string_for_print = ''
    if original_sum >= best_sum:
        string_for_print = f'Best pureness {original_sum} after {0} rotations'
    else:
        string_for_print = f'Best pureness {best_sum} after {rotation + 1} rotations'


    return string_for_print

# test = ([4, 3, 2, 6], 4)
# result = best_list_pureness(*test)
# print(result)
#
#
# test = ([7, 9, 2, 5, 3, 4], 3)
# result = best_list_pureness(*test)
# print(result)

test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
