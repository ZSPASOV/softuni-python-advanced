try:
    file = open('invalid.txt', 'r')  # FileNotFoundError
except FileNotFoundError:
    print("File not found or path is incorrect")
# vinagi se vliza do finally block bez znachenie dali hvurlq greshka ili ne
finally:
    print("exit")
