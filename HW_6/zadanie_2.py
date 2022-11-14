print('Исходная последоватеьность: ', pos := [1, 2, 3, 5, 1, 5, 6, 6, 3, 10])
print('Уникальные элементы: ', [n for n in set(pos) if pos.count(n) == 1])
print('Повторяемые элементы: ', [n for n in set(pos) if pos.count(n) > 1])
print('Последовательность без дубликатов: ', list(set(pos)))