N = int(input('Введите число элементов массива: '))
count_list = []
count_list_str = []
for i in range(0, N):
    count_str = input('Введите значение элемента: ')
    if '.' in count_str:
        count_list.append(count_str.split('.')[1])
    elif ',' in count_str:
        count_list.append(count_str.split(',')[1])
    else:
        count_list.append(0)
    count_list_str.append(count_str)

print(count_list_str)   # например, если мы берём значение 0,3 и 0,03, то эти дробные части будут равны
print(count_list)
