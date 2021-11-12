list_of_clothes = list(map(lambda n: int(n), input().split(' ')))
rack_capacity = int(input())
sum = 0
racks_needed = 0

while list_of_clothes:
    if list_of_clothes[-1] + sum < rack_capacity:
        sum += list_of_clothes[-1]
        list_of_clothes.pop()
    elif list_of_clothes[-1] + sum == rack_capacity:
        sum += list_of_clothes[-1]
        list_of_clothes.pop()
        racks_needed += 1
        sum = 0
    else:
        sum = 0
        sum += list_of_clothes[-1]
        list_of_clothes.pop()
        racks_needed += 1

print(racks_needed)



