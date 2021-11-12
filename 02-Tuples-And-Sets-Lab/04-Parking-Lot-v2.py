n = int(input())
parking = set()

for _ in range(n):
    direction, reg_num = input().split(', ')
    operations = {
        'IN': parking.add,
        'OUT': parking.remove,
    }
    operations[direction](reg_num)

if parking:
    print('\n'.join(parking))
else:
    print('Parking Lot is Empty')