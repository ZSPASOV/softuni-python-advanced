new_list = [2, 3, 4]
fn = new_list.pop
print(type(fn)) # <class 'builtin_function_or_method'>
print(fn) # <built-in method pop of list object at 0x00000000024915C0>
print(fn()) #
print(new_list) # [2, 3]