# Задача 1

# some_weekday = int(input('Введите день недели числом от 1 до 7: '))
# print('Да' if some_weekday in [6, 7] else 'Нет')

# Вариант  2

# day = int(input('Введите цифру, обозначающую день недели: '))
# print('Да' if day in [6, 7] else 'Нет' if day in range(1,6) else 'Это не день недели'

# Вариант 3

# day = int(input('Введите цифру, обозначающую день недели: '))
# match day:
#     case 6 | 7:
#         print('Выходной')
#     case day if 1 <= day <= 5: # case n if n in range(1, 6)
#         print('Будний день')
#     case _:
#         print('Не день недели')

# Задача 2

# for X in 1, None:
#     for Y in 0, 1:
#         for Z in 0, 1:
#             print(X, Y, Z)
#             print('Истина' if not (X or Y or Z) == (not X and not Y and not Z) else 'Ложь')

# Вариант 2

# s = range(2)
# res = True

# for x in s:
#     for y in s:
#         for z in s:
#             if not (not(x or y or z) == (not x and not y and not z)):
#                 res = False
#                 break
# print(res)

# Варант 3

# res = (not (x or y or z) == (not x and not y and not z) for z in range(2)
#         for y in range(2) for x in range(2))
# print(type(res)) # res - генератор
# print(all(res)) # оператор all возвращает истину
#                 # если все элементы истинны,
#                 # если хотя бы один ложь, то all возвращает ложь.
#                 # имеется оператор any который возвращает истину,
#                 # если хотя бы один элемент - истина
# print(*res, sep='\n')
# print(*res, sep='\n') # генератор звполняет на лету и тут же их забывает

# Вариант 4

from itertools import product

print(all(not(x or y or z) == (not x and not y and not z) 
          for x, y, z in product(*((True, False),) * 3, )))

# Задача 3

# x = int(input('Введите значение на оси х: '))
# y = int(input('Введите значение на оси y: '))
# if x == y or x == 0 or y == 0:
#     print('Что то пошло не так!')
# if x > 0 < y:
#     print('Первая четверть')
# elif x < 0 < y:
#     print('Вторая четверть')
# elif x > 0 > y:
#     print('Третья четверть')
# else: print('Четвёртая четверть')

# Задача 4
# sqr_2D = int(input('Введите номер четверти: '))
# if sqr_2D == 1:
#     print('x > 0, y > 0')
# elif sqr_2D == 2:
#     print('x < 0, y > 0')
# elif sqr_2D == 3:
#     print('x > 0, y < 0')
# else: print('x < 0, y < 0')

# Задача 5

# A = input('Введите координату первой точки (x и у через запятую): ')
# B = input('Введите координату второй точки: ')
# length = ((int(B.split(',')[0]) - int(A.split(',')[0])) ** 2 
# + (int(B.split(',')[1]) - int(A.split(',')[1])) ** 2) ** (1/2) # в степени 1/2
# print(round(length, 3))
