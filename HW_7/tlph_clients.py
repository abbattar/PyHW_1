def get_name(id):
    return input('Введите имя пользователя: ')

def get_scnd_name(id):
    return input('Введите ффамилию пользователя: ')

def get_workplace(id):
    return input('Введите место работы: ')

def get_brth_date(id):
    return input('Введите день рождения: ')

def get_tlph_number(id):
    j = int(input('Сколько телефонов?: '))
    tlph = []
    if j > 1:
        for i in range(0, j):
            tmp = input(f'Введите номер {i+1}-го телефона : ')
            tlph += [tmp]
        return tlph
    elif j == 1:
        return input('Введите номер телефона: ')
    else:
        print('Не балуйся')

# tlph_number = get_tlph_number()
# print(tlph_number)

def get_id():
    global user_id
    user_id = int(input('id = '))
    return user_id

# def all_in_one(id):
#     return [get_name(id), get_scnd_name(id), get_workplace(id),
#             get_brth_date(id), get_tlph_number(id)]

# userid = get_id()
# print(all_in_one(userid))