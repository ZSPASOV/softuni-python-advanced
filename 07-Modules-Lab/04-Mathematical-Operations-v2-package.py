from mathoperations import parser, executor


expr = input()
res = executor.exec(*parser.parse_expr(expr))
print(res)