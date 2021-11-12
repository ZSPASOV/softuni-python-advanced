def find_strongest_eggs(eggs, sub_list_count):
    best_eggs = []

    for i in range(sub_list_count):
        current = [eggs[idx] for idx in range(i, len(eggs), sub_list_count)]
        mid_element = current[len(current) // 2]
        left_element = current[len(current) // 2 - 1]
        right_element = current[len(current) // 2 + 1]
        if left_element < mid_element > right_element > left_element:
            best_eggs.append(mid_element)

    return best_eggs

test = ([-1, 7, 3, 15, 2, 12], 2)
print(find_strongest_eggs(*test))
# output [3, 15]

# We should create 2 sub lists:
# [-1, 3, 2] => 3 is bigger than -1 and 2, and 2 is bigger than -1, so we return 3 as
# an egg which fulfills the above requirements
# [7, 15, 12] => 15 is bigger than 7 and 12, and 12 is bigger than 7, so we return 15

test = ([-1, 0, 2, 5, 2, 3], 2)
print(find_strongest_eggs(*test))
# output [5]
# We should create 2 sublists ([-1, 2, 2], [0, 5, 3]) from
# the provided sequence and check whether each of them meets the given conditions.
# Since 2 is not bigger that 2 we don’t include it in the final result and continue
# with the second sub list.

test = ([51, 21, 83, 52, 55], 1)
print(find_strongest_eggs(*test))
# output [83]

# 83 is bigger than 52 and 21 so we continue to check the second condition.
# 52 is bigger than 21 and 55 is bigger than 51, so we consider 83 as stronger egg.

