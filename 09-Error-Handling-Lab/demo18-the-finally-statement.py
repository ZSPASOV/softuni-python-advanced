# If a finally clause is present, the finally clause will execute as the last task before the try statement completes
# The finally clause runs whether or not the try statement produces an exception

try:
    x = int('Peter')
except ValueError:
    print('Cannot convert str to int')
finally:
    print('Finally block')