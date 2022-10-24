# Задайте натуральное число n.
# Напишите программу, которая составит список простых множителей числа n

n = int(input('Введите какое-то натуральное число больше 3: '))

# Решето Эратосфена для нахождения простых чисел


def primes(n):
    sieve = [True] * n
    for i in range(3, int(n**0.5)+1, 2):
        if sieve[i]:
            sieve[i*i::2*i] = [False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]


print(primes(n))

# 2 примера 1-й из урока, второй подсмотрел в интернете до урока
prime = []
for i in primes(n):
    prime = primes(i)   # работает без append O_o
res = []
tmp = n
i = 0
while tmp > 1:
    if not (tmp % int(prime[i])):
        tmp //= prime[i]
        res.append(prime[i])
    else:
        i += 1
print('{} равно произведению чисел {}'.format(n, res))

m = n
factors = []
d = 2
while d*d <= n:
    if not (n % d):
        factors.append(d)
        n //= d
    else:
        d += 1
factors.append(n)
# if len(factors) == 1:
#     print('Это и есть простое число')
# else:
print('{} равно произведению чисел {}'.format(m, factors))
