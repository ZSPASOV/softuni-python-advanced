from collections import deque

availability = int(input())

orders = deque([int(i) for i in input().split(' ')])
biggest_order = max(orders)
for i in range(len(orders)):
    if orders[0] <= availability:
        order_value = orders.popleft()
        availability -= order_value
        if order_value > biggest_order:
            biggest_order = order_value
    else:
        break

print(biggest_order)
if orders:
    print(f'Orders left: {" ".join([str(i) for i in orders])}')
else:
    print('Orders complete')
