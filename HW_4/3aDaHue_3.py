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

# 2 cпособа при которых не теряется сортировка исходного списка


def f(li_st):
    n = []
    for i in li_st:
        if i not in n:
            n.append(i)
    return n


print(f(lis_t))


def unique(obj: iter):
    args = []
    for a in obj:
        if a not in args:
            args.append(a)
            yield a


r = unique(lis_t)
print([*r])
