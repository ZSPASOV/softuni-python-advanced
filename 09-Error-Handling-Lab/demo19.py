try:
    #int('baba')
    '2' + 2
    print('successs')
except(RuntimeError, ValueError, TypeError):
    print('error happened')