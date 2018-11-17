board = [[0,0,0],[0,0,0],[0,0,0]]
player = 1
i=0
while i<9:
    for row in board:
        for elem in row:
            print(elem, end=" ")
        print()
    if player==1:
        message = "Player First"
        fishka = "X"
        player=2
    elif player==2:
        message = "Player Second"
        fishka = "Y"
        player=1
    print("Next {}".format(message))
    x = int(input("enter row->"))-1
    y = int(input("enter column->"))-1
    board[x][y] = fishka
    i+=1
