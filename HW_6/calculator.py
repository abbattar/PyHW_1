# Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.

# import re
#
#
# def num(expr):
#     expr = expr.lstrip()
#     res = re.match("^[+-]?\d(\.\d+)?", expr)
#     if res:
#         return float(res.group(0)), expr[res.end():]
#     else:
#         return None, expr
#
# def value(expr):
#     res, rest = num(expr)
#     if res != None:
#         return res, rest
#     res, rest = grouping(expr)
#     return res, rest
#
# def grouping(expr):
#     expr = expr.lstrip()
#     rest = ""
#     if expr[0] == "(":
#         rest = expr[1:]
#     else:
#         return None, expr
#     numb, rest = term(rest)
#     if rest[0] != ")":
#         return None, expr
#     return numb, rest[1:]
#
# def mul_oper(expr):
#     expr = expr.lstrip()
#     res = re.match("[*/]", expr)
#     if res:
#         return res.group(0), expr[res.end():]
#     else:
#         return None, expr
#
# def mul(expr):
#     numb1, rest1 = value(expr)
#
#     if numb1 == None:
#         return None, expr
#
#     op, rest2 = mul_oper(rest1)
#
#     if op == None:
#         return numb1, rest1
#
#     numb2, rest2 = mul(rest2)
#
#     if op == "*":
#         return numb1 * numb2, rest2
#     if op == "/":
#         return numb1 / numb2, rest2
#
#     return None, expr
#
# def sum_oper(expr):
#     expr = expr.lstrip()
#     res = re.match("[+-]", expr)
#     if res:
#         return res.group(0), expr[res.end():]
#     else:
#         return None, expr
#
# def sum(expr):
#     numb1, rest1 = mul(expr)
#
#     if numb1 == None:
#         return None, expr
#
#     op, rest2 = sum_oper(rest1)
#
#     if op == None:
#         return numb1, rest1
#
#     numb2, rest2 = sum(rest2)
#
#     if op == "+":
#         return numb1 + numb2, rest2
#     if op == "-":
#         return numb1 - numb2, rest2
#
#     return None, expr
#
# def term(expr):
#     return sum(expr)
#
# h = input('Введите математическое выражение: ')
# print(term(h))

import re

actions = {
    "^": lambda x, y: str(float(x) ** float(y)),
    "*": lambda x, y: str(float(x) * float(y)),
    "/": lambda x, y: str(float(x) / float(y)),
    "+": lambda x, y: str(float(x) + float(y)),
    "-": lambda x, y: str(float(x) - float(y))
}

priority_reg_exp = r"\((.+?)\)"
action_reg_exp = r"(-?\d+(?:\.\d+)?)\s*\{}\s*(-?\d+(?:\.\d+)?)"

def my_eval(expresion: str) -> str:
    while (match := re.search(priority_reg_exp, expresion)):
        expresion: str = expresion.replace(match.group(0), my_eval(match.group(1)))

    for symbol, action in actions.items():
        while (match := re.search(action_reg_exp.format(symbol), expresion)):
            expresion: str = expresion.replace(match.group(0), action(*match.groups()))

    return expresion

exp = input('Введите математическое выражение: ')
print(my_eval(exp), eval(exp))