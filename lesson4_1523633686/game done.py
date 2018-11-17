from os import system, name
cls = "cls" if name == "nt" else "clear"
from random import randint
board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]
chip = ["X", "O"]
i = 0
win = 0
stop = 0
computer = [0, 0]

# start menu
while True:
    system(cls)
    print("  1 2 3")
    print("1 X|O|X   Выберите режим игры")
    print(" -------  Игрок против игрока: 1")
    print("2 O|X|O   Игрок 2 - компьютер: 2")
    print(" -------  Игрок 1 - компьютер: 3")
    print("3 X|O|X   Для выхода введите 'е'")
    choise = input("Ваш выбор: ")
    if choise == "e":
        stop = 1
        break
    elif choise == "1":
        break
    elif choise == "2":
        computer[1] = 1
        break
    elif choise == "3":
        computer[0] = 1
        break

if not stop:
    while True:
        gamer = i % 2
        # interface
        system(cls)
        print("  1 2 3")
        print("1 {0[0][0]}|{0[0][1]}|{0[0][2]}   Игрок: {1}".format(board, gamer + 1))
        print(" -------  Фишка: {}".format(chip[gamer]))
        print("2 {0[1][0]}|{0[1][1]}|{0[1][2]}   Для хода введите номера".format(board))
        print(" -------  строки и столбца (например: 22)")
        print("3 {0[2][0]}|{0[2][1]}|{0[2][2]}   Для выхода введите 'е'".format(board))

        if win == 1:
            print("Победил игрок {}".format(gamer + 1))
            break
        elif win == -1:
            print("Ничья")
            break
        # input
        if computer[gamer]:
            while True:
                x, y, = randint(0, 2), randint(0, 2)
                if board[x][y] == " ":
                    break
        else:
            xy = input("Ваш ход: ")
            # checking input
            if xy == "e":
                break  # exit game
            if len(xy) != 2:
                continue
            try:
                x, y = int(xy[0])-1, int(xy[1])-1
            except:
                continue
            if x > 2 or y > 2 or board[x][y] != " ":
                continue
        board[x][y] = chip[gamer]
        # check for win
        for index in [0, 1, 2]:
            if board[index][0] == board[index][1] == board[index][2] != " ":
                win = 1
                continue
            if board[0][index] == board[1][index] == board[2][index] != " ":
                win = 1
                continue
        if win:
            continue
        if board[0][0] == board[1][1] == board[2][2] != " " or board[0][2] == board[1][1] == board[2][0] != " ":
            win = 1
            continue
        i += 1
        if i > 8:
            i -= 1
            win = -1
            continue

