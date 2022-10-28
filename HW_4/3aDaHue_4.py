from random import randint
k = int(input('Введите степень многочлена: '))

lst_polinome = []
for i in range(0, k+1):
    lst_polinome.append(randint(0,100))
if lst_polinome[k] == 0:
    print('По независящим от нас причинам произошла ошибка', lst_polinome[k])
    exit()
else:
    # path = './HW_4/polinome.txt'
    with open(r"./HW_4/polinome.txt", 'w') as file:
        str_line =[]
        str_line.append(str(lst_polinome[0]))
        str_line.append(str(f'{lst_polinome[1]}*x'))
        for i in range(2,k+1):
            str_line.append( f'*x^{i}')
            str_line[i] = str(lst_polinome[i]) + str_line[i]
        file.write(" + ".join(str_line))  # Если перевернуть строку,
    # то число ху будет ух, поэтому воспользуемся коммутативным правилом =))