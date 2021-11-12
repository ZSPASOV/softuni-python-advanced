# lambda funkciite mogat da sudurzhat v sebe si i drugi lambda funkcii

fn = lambda a: lambda b: a + b

print(fn(1)(2)) # 3

# bez lambda sushtoto bi izglejdalo taka:
def baba(a):
    def dqdo(b):
        return a + b
    return dqdo

print(baba(1)(2))