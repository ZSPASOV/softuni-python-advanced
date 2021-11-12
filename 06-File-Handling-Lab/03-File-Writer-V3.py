f = open('my_first_file_v3.txt', 'w')
try:
    f.write('I just created my first file.') # some error is being thrown, e.g. OutOfSpaceError
finally:
    f.close()