# It is possible to write programs that handle selected exceptions
while True:
    try:
        x = int(input('Please enter a number: '))
        break
    except ValueError:
        print('Oops! That was no valid number. Try again...')