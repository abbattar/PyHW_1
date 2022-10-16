# Как на занятии, но почему то не пошло
from random import randint


N = int(input('Введите положительное целое число: '))
rand_numbers = []
for i in range(-N, N):
    if i == 0:
        rand_numbers[i] = randint(-20, 20)
    else:
        rand_numbers.append(randint(-20, 20))
print(rand_numbers)
# exit()
mult = 1
some_lst = []

with open('tfile.txt', 'r') as file:            # FileNotFoundError: 
                                                # [Errno 2] No such file 
                                                # or directory: 'file.txt' хотя этот файл в папке есть
    for line in file:
        if -len(rand_numbers) < int(line) < len(rand_numbers):
            mult *= rand_numbers[int(line)]
            some_lst.append(rand_numbers[int(line)])

print('Новый набор: ', some_lst)
print('Произведение чисел: ', mult if mult != 0 else 'Таких значений нет')
