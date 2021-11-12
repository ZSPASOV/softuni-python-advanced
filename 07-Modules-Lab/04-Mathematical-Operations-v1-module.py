import mathops

expr = input()
mathops.parse_expr(expr)
res = mathops.exec(*mathops.parse_expr(expr))
print(res)

