from random import randint
k = int(input('Введите степень многочлена: '))

str_polinome = []
for i in range(k+1):
    str_polinome.append(randint(0,100))
if str_polinome[k] == 0:
    print('По независящим от нас причинам произошла ошибка', str_polinome[0])
    exit()
else:
    # path = './HW_4/polinome.txt'
    with open(r"./HW_4/polinome.txt", 'w') as file:
        str_line =[]
        str_line.append(str(str_polinome[0]))
        for i in range(1, k+1):
            str_line.append( f' * {i}^x')
            str_line[i] = str(str_polinome[i]) + str_line[i]
        file.write("Polinome = "+" + ".join(str_line)[::-1])