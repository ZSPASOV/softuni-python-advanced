with open('some_file_where_we_print.txt', 'w') as f:
    for i in range(100):
        print(str(i), file=f) # ako ne dadem file=f shte printva v konzolata prosto