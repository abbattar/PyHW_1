N = int(input('Введите число элементов массива: '))
from random import randint
rand_numbers = []
sum_numbers = 0
for i in range(0, N):
    rand_numbers.append(randint(0, 20))
    if i % 2 == 0:
        sum_numbers = sum_numbers + int(rand_numbers[i])
print(rand_numbers)
print(sum_numbers)