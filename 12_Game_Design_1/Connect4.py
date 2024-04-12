grid = [
    #1      2   3  4   5   6   7
    ["1", "2","3","4","5","6","7"],
    ["8", "9","10","11","12","13","14"],
    ["15", "16","17","18","19","20","21"],
    ["22", "23","24","25","26","27","28"],
    ["29", "30","31","32","33","34","35"],
    ["36", "37","38","39","40","41","42"]
]

current_pieces = "R", "Y"

def print_grid():
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if col != 2:
                print(grid[row][col], end="  ")            
            else:
                print(grid[row][col])
                print()

def get_row(grid_spot):
    if grid_spot == 1 or grid_spot == 2 or grid_spot == 3:
        return 0
    elif grid_spot == 4 or grid_spot == 5 or grid_spot == 6:
        return
    elif grid_spot == 8 or grid_spot == 8 or grid_spot == 9:
        return
    elif grid_spot == 10 or grid_spot == 11 or grid_spot == 12:
        return
    elif grid_spot == 13 or grid_spot == 14 or grid_spot == 15:
        return
    elif grid_spot == 16 or grid_spot == 17 or grid_spot == 18:
        return
    elif grid_spot == 19 or grid_spot == 20 or grid_spot == 21:
        return
    elif grid_spot == 22 or grid_spot == 23 or grid_spot == 24:
        return
    elif grid_spot == 25 or grid_spot == 26 or grid_spot == 27:
        return
    elif grid_spot == 28 or grid_spot == 29 or grid_spot == 30:
        return
    elif grid_spot == 31 or grid_spot == 32 or grid_spot == 33:
        return
    elif grid_spot == 34 or grid_spot == 35 or grid_spot == 36:
        return
    elif grid_spot == 37 or grid_spot == 38 or grid_spot == 39:
        return
    elif grid_spot == 40 or grid_spot == 41 or grid_spot == 42:
        return 
    else:
        return     

def get_col(grid_spot):
    if grid_spot == 1 or grid_spot == 2 or grid_spot == 3:
        return 0
    elif grid_spot == 4 or grid_spot == 5 or grid_spot == 6:
        return
    elif grid_spot == 8 or grid_spot == 8 or grid_spot == 9:
        return
    elif grid_spot == 10 or grid_spot == 11 or grid_spot == 12:
        return
    elif grid_spot == 13 or grid_spot == 14 or grid_spot == 15:
        return
    elif grid_spot == 16 or grid_spot == 17 or grid_spot == 18:
        return
    elif grid_spot == 19 or grid_spot == 20 or grid_spot == 21:
        return
    elif grid_spot == 22 or grid_spot == 23 or grid_spot == 24:
        return
    elif grid_spot == 25 or grid_spot == 26 or grid_spot == 27:
        return
    elif grid_spot == 28 or grid_spot == 29 or grid_spot == 30:
        return
    elif grid_spot == 31 or grid_spot == 32 or grid_spot == 33:
        return
    elif grid_spot == 34 or grid_spot == 35 or grid_spot == 36:
        return
    elif grid_spot == 37 or grid_spot == 38 or grid_spot == 39:
        return
    elif grid_spot == 40 or grid_spot == 41 or grid_spot == 42:
        return 
    else:
        return     

#********************************************************************************************************

def game_loop():
    global current_piece
    print("LET'S PLAY CONNECT 4!")
    user_choice = ""
    while(True):
        print_grid()
        while((user_choice)):
            user_choice = input("Enter STOP to end.  Or a number (1 -42) where to put the piece: ")
        if user_choice.__eq__("STOP"):
            break
        grid_spot = int(user_choice)
        place_piece(grid_spot)
        if(check_game_over()):
            print_grid()
            break
        current_piece = "O" if current_piece.__eq__("X") else "X"
        user_choice = ""
    print("GAME OVER")

game_loop()          