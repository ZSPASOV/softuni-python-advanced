a = 1

def baba():
    global a
    a += 1

baba()

print(a) # 2

b = 5

def dqdo():
    print(b)

dqdo() # 5

# nujno e da pishem global samo kogato v funkciq mutirame promenlivi ot globalniq scope