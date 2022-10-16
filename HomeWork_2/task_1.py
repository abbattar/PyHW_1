flo_at = input('Введите вещественное число: ')
numbers_arr = flo_at.split('.')

if len(numbers_arr) != 1:
    full_num = numbers_arr[0] + numbers_arr[1]
else:
    full_num = numbers_arr[0]
print(full_num)
print(type(full_num))
if '-' in full_num:
    full_num = full_num.replace('-', '')
print(full_num)

sum_nums = 0
for i in full_num:
    sum_nums = int(i) + sum_nums
print(sum_nums)

# Из урока

# print(sum(map(int, (c for c in input('Введите некое число:') if c.isdigit()))))