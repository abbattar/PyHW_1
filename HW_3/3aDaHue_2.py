from random import randint
N = int(input('Введите число элементов массива: '))
rand_numbers = []
mult_numbers = []
for i in range(0, N):
    rand_numbers.append(randint(0, 10))
for i in range(0, N//2):
    mult_numbers.append(rand_numbers[i] * rand_numbers[-i - 1])

print(rand_numbers)
print(mult_numbers)
