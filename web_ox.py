Grid = [ [0, 0, 0],
         [0, 0, 0],
         [0, 0, 0] ]
turn = "x" 

def fil_spot(row,col):
    global turn
    if turn == "o":
        turn = "x"
    else:
        turn = "o"
    Grid[row][col] = turn
    for line in Grid:
        print(line)


def choose_spot():
    while True:
        row = int(input("choose a row:"))
        col = int(input("choose a col:"))
        chosen = Grid[row][col]
        if chosen != 0:
            print("this spot is full" , chosen)
            choose_spot()
        else:
            fil_spot(row,col)
for element in Grid:
    if 0 in element:
        choose_spot()
    else:
       print("board is full")
       exit()
