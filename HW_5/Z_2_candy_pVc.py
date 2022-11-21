from random import randint
from secrets import choice

message = ['твоя очередь', 'да бери уже', 'бери больше', 'не корову проигрываешь',
           'бери быстрее', 'да хорош, так долго думать уже']

def player_vs_bot():
    candies_total = 2021
    max_take = 28
    player_1 = input('\nКак тебя зовут?: ')
    player_2 = 'Компьютер'
    players = [player_1, player_2]
    print(f'\nНу чтож {player_1} и {player_2} да начнется игра !\n')
    print('\nДля начала опеределим кто первый начнет игру.\n')

    lucky = randint(0, 1)

    print(f'Поздравляю {players[lucky]} ты ходишь первым !')

    while candies_total > 0:
        lucky += 1

        if not lucky % 2:
            print(
                f'\nХодит {players[1]} \nНа кону {candies_total}. \n{choice(message)}: ')

            if candies_total < 29:
                step = candies_total
            else:
                delenie = candies_total//28
                step = candies_total - ((delenie*max_take)+1)
                if step == -1:
                    step = max_take -1
                if step == 0:
                    step = max_take
            while 1 > step or step > 28:
                step = randint(1,29)
            print(step)
        else:
            step = int(input(f'\nНу чтож ходи, {players[0]} \nНа кону {candies_total} {choice(message)}:  '))
            while step > max_take:
                step = int(input(f'\nЗа один ход можно взять {max_take} конфет, попробуй еще раз: '))
        candies_total = candies_total - step

    print(f'На кону осталось {candies_total} \nПобедил {players[lucky%2]}')

player_vs_bot()