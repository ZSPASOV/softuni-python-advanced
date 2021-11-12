stack = input().split(' ')
empty_str = ''

for _ in range(len(stack)):
    empty_str += stack.pop() + ' '
print(empty_str)

