n = int(input('Введите положительное целое число: '))
n_array =[]
sum_n_array = 0
for i in range(1, n + 1):
    n_array.append((1 + 1/i)**i)
    sum_n_array += float(n_array[i - 1])
print(sum_n_array)