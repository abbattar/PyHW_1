import re
from sympy import Symbol, collect


def convert(line):
    line = re.sub(r'(\d)(x)', r'\1*\2', line)
    line = line.replace('^', '**')
    line = line[:-4:]
    return line
with open('./HW_4/polinome1.txt', 'r') as data1:
    record1 = data1.readline()

with open('./HW_4/polinome2.txt', 'r') as data2:
    record2 = data2.readline()

print(f'Первый многочлен: {record1}')
print(f'Второй многочлен: {record2}')

x = Symbol('x')

result = str(collect(record1 + ' + ' + record2, x))
result = result.replace('**', '^')
result = result.replace('*', '')
result = result + ' = 0'

with open('./HW_4/polinome3.txt', 'w') as data3:
    data3.write(result)