input_list = [int(x) for x in input().split()]
even_numbers = list(filter((lambda x: x % 2 == 0), input_list))
print(even_numbers)



