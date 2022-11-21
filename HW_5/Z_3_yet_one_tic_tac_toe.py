look_Board = {'1': '',
              '2': '',
              '3': ''}

look_keys = []

for key in look_Board:
    look_keys.append(key)


def printLookBoard(board):
    print(board['1'] + '1|2|3')
    print('-+-+-')
    print(board['2'] + '4|5|6')
    print('-+-+-')
    print(board['3'] + '7|8|9')


theBoard = {'1': ' ', '2': ' ', '3': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '7': ' ', '8': ' ', '9': ' '}

board_keys = []

for key in theBoard:
    board_keys.append(key)


def printBoard(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])


def game():
    printLookBoard(look_Board)

    print()

    turn = 'X'
    count = 0

    for i in range(10):
        printBoard(theBoard)
        if i == 0:
            print('Начинаем, ход Х')
        else:
            print("Ваш ход принят, Следующий игрок: ", turn)

        move = input()

        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
        else:
            print("Здесь кто то есть!\nДавай другую позицию")
            continue

        if count >= 5:
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ':
                printBoard(theBoard)
                print("\nВсё.\n")
                print(" **** " + turn + " выиграл. ****")
                break
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ':
                printBoard(theBoard)
                print("\nВсё.\n")
                print(" **** " + turn + " выиграл. ****")
                break
            elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ':
                printBoard(theBoard)
                print("\nВсё.\n")
                print(" **** " + turn + " выиграл. ****")
                break
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ':
                printBoard(theBoard)
                print("\nВсё.\n")
                print(" **** " + turn + " выиграл. ****")
                break
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ':
                printBoard(theBoard)
                print("\nВсё.\n")
                print(" **** " + turn + " выиграл. ****")
                break
            elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ':
                printBoard(theBoard)
                print("\nВсё.\n")
                print(" **** " + turn + " выиграл. ****")
                break
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ':
                printBoard(theBoard)
                print("\nВсё.\n")
                print(" **** " + turn + " выиграл. ****")
                break
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ':
                printBoard(theBoard)
                print("\nВсё.\n")
                print(" **** " + turn + " выиграл. ****")
                break

        if count == 9:
            print("\nВсё!.\n")
            print("Ничья!!")

        if turn == 'X':  # Меняем значение
            turn = 'O'
        else:
            turn = 'X'

    restart = input("Ещё разочек?(y/n) (д/н)")
    if restart == "y" or restart == "Y" or restart == "д" or restart == "Д":
        for key in board_keys:
            theBoard[key] = " "

        game()


# Честно списал с интернета, немного переделав, поэтому не знаю,
# что означают следующие строчки:
if __name__ == "__main__":
    game()
