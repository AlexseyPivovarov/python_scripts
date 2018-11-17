from os import system, name
cls = "cls" if name == "nt" else "clear"
board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]
chip = ["X", "O"]
i = 0
win = 0

while True:
    gamer = i % 2
    # interface
    system(cls)
    print("  1 2 3")
    print("1 {0[0][0]}|{0[0][1]}|{0[0][2]}   Игрок: {1}".format(board, gamer + 1))
    print(" -------  Ваша фишка: {}".format(chip[gamer]))
    print("2 {0[1][0]}|{0[1][1]}|{0[1][2]}   Для хода введите номера строки и столбца (например: 22)".format(board))
    print(" -------  Для выхода введите 'е'")
    print("3 {0[2][0]}|{0[2][1]}|{0[2][2]}".format(board))

    if win == 1:
        print("Победил игрок {}".format(gamer + 1))
        break
    elif win == -1:
        print("Ничья")
        break
    # input
    xy = input("Ваш ход: ")

    # checking input
    if xy != "e":
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
    else:  # exit game
        break
