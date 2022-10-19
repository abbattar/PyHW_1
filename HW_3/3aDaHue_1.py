N = int(input('Введите число элементов массива: '))
from random import randint
rand_numbers = []
sum_numbers = 0
for i in range(N):
    rand_numbers.append(randint(0, 20))
for i in range(1, N, 2):
    sum_numbers += int(rand_numbers[i])
print(rand_numbers)
print(sum_numbers)