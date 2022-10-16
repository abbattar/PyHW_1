N = int(input('Введите положительное целое число: '))
# factorial_N = []

# n = 1
# factorial_n = 1
# while n <= N:
#     factorial_n *= n
#     n += 1
#     factorial_N.append(factorial_n)

# print(factorial_N)

# Через рекурсивную анонимную функцию λ (из занятия)

# factorial = lambda x: x if x == 1 else x * factorial(x - 1)
# print([factorial(i) for i in range(1, N + 1)])

# ~~~ yeld ~~~

def fact(N):
    last = 1
    for i in range(1, N + 1):
        last *= i
        yield last
lst = list(fact(N))
print(lst)