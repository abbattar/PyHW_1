import html_generator as hg

all_users = int(input('Всего людей: '))

for i in range(0, all_users):
    user = input(f'Ник {i+1}-го пользователя: ')
    print(f'{hg.create(user, i)}\n')
    i += 1
