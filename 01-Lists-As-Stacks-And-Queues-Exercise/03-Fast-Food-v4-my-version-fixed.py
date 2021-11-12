from collections import deque

amount_of_food = int(input())
orders = deque(list(map(lambda n: int(n), input().split(' '))))
print(max(orders)) # nqma nujda 2 pyti da go pishes po dolu

while orders:
    if amount_of_food >= orders[0]:
        amount_of_food -= orders.popleft()
    else:
        # print(max_order)
        # orders_list_str = [str(x) for x in orders]
        # orders_str = ''
        # for i in orders_list_str:
        #     orders_str += i + ' '
        print(f'Orders left: {" ".join([str(x) for x in orders])}')
        break
#
if len(orders) == 0:
    # print(max_order)
    print('Orders complete')