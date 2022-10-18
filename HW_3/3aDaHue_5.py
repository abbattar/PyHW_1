def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
k = 8
fib_arr = []
for i in range(-k, k + 1):
    if i < 0:
        fib_arr.append((-1)**(i + 1) * fib(abs(i)))
    elif i > 0:
        fib_arr.append(fib(i))
    else:
        fib_arr.append(0)
print(fib_arr)
