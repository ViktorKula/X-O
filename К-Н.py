board = list(range(1, 10))

victory = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]


def draw_board():
    for i in range(3):
        print(board[0 + i * 3], board[1 + i * 3], board[2 + i * 3])


def number(player):
    while True:
        value = input('Выберите ячейку: ' + player + '?')
        if not (value in '123456789'):
            print('Неверная цифра.'
                  'Выбирайте от 1 до 9.')
            continue
        value = int(value)
        if str(board[value - 1]) in 'XO':
            print('Ячейка занята')
            continue
        board[value - 1] = player
        break


def win():
    for v in victory:
        if (board[v[0] - 1]) == (board[v[1] - 1]) == (board[v[2] - 1]):
            return board[v[1] - 1]
    else:
        return False


def game():
    counter = 0
    while True:
        draw_board()
        if counter % 2 == 0:
            number('X')
        else:
            number('O')
        if counter > 3:
            winner = win()
            if winner:
                draw_board()
                print(winner, 'выйграл!')
                break
        counter += 1
        if counter > 8:
            draw_board()
            print('Ничья')
            break


game()
