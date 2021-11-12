import operator


def parse_expr(expr):
    n1, sign, n2 = expr.split()
    op = {
        '/': operator.truediv,
        '*': operator.mul,
        '+': operator.add,
        '-': operator.sub,
        '^': operator.pow,
    }[sign] # this is shorter syntax. taka rechnika ne se pazi, a ima direktno referenciq kum rechnika i posle se izchistva ot pametta
    # you can use instead:
    # ops = {
    #     '/': operator.truediv,
    #     '*': operator.mul,
    #     '+': operator.add,
    #     '-': operator.sub,
    #     '^': operator.pow,
    # }[sign]
    # op = ops[sign] - taka se pazi i rechnika i posle se referira kum nego
    return op, float(n1), float(n2)