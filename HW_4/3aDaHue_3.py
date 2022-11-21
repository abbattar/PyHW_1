from random import randint
length_list = int(input('Задайте длину списка: '))
lis_t = []
for i in range(0, length_list):
    lis_t.append(randint(0, 20))
print(lis_t)
lis_t_filt = list(set(lis_t))   # Способ, при котором не только удаляются все
# одинаковые элементы списка, но и меняется их
# последовательность => от меньшего к большему
print(lis_t_filt)

n = []
for i in lis_t:
    if i not in n:
        n.append(i)

number_list = list(map(int, lis_t))
lis_t = [i for i in n if number_list.count(i) == 1]
# for i in range(0,len(n)):
#     if n[i] in lis_t:
#         lis_t.pop(i)

print(n)
print(lis_t)