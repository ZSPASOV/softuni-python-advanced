number_inputs = int(input())
stack = []

for _ in range(number_inputs):
    query = input().split(' ')
    command = int(query[0])
    if command == 1:
        element = int(query[1])
        stack.append(element)
    elif command == 2 and len(stack) > 0:
        stack.pop()
    elif command == 3 and len(stack) > 0:
        print(max(stack))
    elif command == 4 and len(stack) > 0:
        print(min((stack)))

stack_for_print = []
for _ in range(len(stack)):
    element_to_append = stack.pop()
    stack_for_print.append(str(element_to_append))

print(', '.join(stack_for_print))
