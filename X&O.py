board = list(range(1, 10))

wins = [(1, 2, 3,), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]


def draw_bora():
    print('-------------')
    for i in range(3):
        print('|', board[0 + i * 3], '|', board[1 + i * 3], '|', board[2 + i * 3], '|')
        print('-------------')


def player_input(player_choice):
    while True:
        value = input('Куда поставить ' + player_choice + " ? ")
        if not (value in "123456789"):
            print("неправильный ввод, Повторите")
            continue
        value = int(value)
        if str(board[value - 1]) in 'XO':
            print('Клетка занята')
            continue
        board[value - 1] = player_choice
        break


def chek_win():
    for each in wins:
        if (board[each[0] - 1]) == (board[each[1] - 1]) == (board[each[2] - 1]):
            return board[each[1] - 1]
    else:
            return False


def main():
    counter = 0
    while True:
        draw_bora()
        if counter % 2 == 0:
            player_input('X')
        else:
            player_input('O')
        if counter > 3:
            winner = chek_win()
            if winner:
                draw_bora()
                print(winner, 'Выйграл')
                break
        counter += 1
        if counter > 8:
            draw_bora()
            print('Ничья')
            break

main()