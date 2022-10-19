N = int(input('Введите число элементов массива: '))
count_list = []
count_list_str = []
for i in range(0, N):
    count_str = float(input('Введите значение элемента: '))
    count_list.append(count_str)
    count_list_str.append(count_list[i] % 1)
    max_count, min_count = count_list_str[0], count_list_str[0]
    for j in count_list_str:
        if float(j) > max_count:
            max_count = j
        if float(j) < min_count:
            min_count = j
div_count = max_count - min_count
print(count_list_str)
print(round(div_count, 3))
# Не работает для отрицательных чисел