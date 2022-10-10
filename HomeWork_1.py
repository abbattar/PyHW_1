# Задача 1
# some_weekday = int(input('Введите день недели числом от 1 до 7: '))
# print('Да' if some_weekday == 6 or some_weekday == 7 else 'Нет')

# Задача 2
# for X in [False, True]:
#     for Y in [True, False]:
#         for Z in [0, 1]:
#             print('Истина' if not (X or Y or Z) == (
#                 not X and not Y and not Z) else 'Ложь')

# Задача 3
# x = int(input('Введите значение на оси х: '))
# y = int(input('Введите значение на оси y: '))
# if x == y or x == 0 or y == 0:
#     print('Что то пошло не так!')
# if x > 0 and y > 0:
#     print('Первая четверть')
# elif x < 0 and y > 0:
#     print('Вторая четверть')
# elif x > 0 and y < 0:
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
import math

A = input('Введите координату первой точки (x и у через запятую): ')
B = input('Введите координату второй точки: ')
length = math.sqrt((int(B.split(',')[0]) - int(A.split(',')[0])) ** 2 + (int(B.split(',')[1]) - int(A.split(',')[1])) ** 2)
print(round(length, 3))