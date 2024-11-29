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
    print(Grid)


def choose_spot():
    while True:
        row = int(input("choose a row:"))
        col = int(input("choose a col:"))
        fil_spot(row,col)
       
choose_spot()
