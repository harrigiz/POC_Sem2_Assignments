grid = [
    #1      2   3  4   5   6   7
    ["1", "2","3","4","5","6","7"],
    ["8", "9","10","11","12","13","14"],
    ["15", "16","17","18","19","20","21"],
    ["22", "23","24","25","26","27","28"],
    ["29", "30","31","32","33","34","35"],
    ["36", "37","38","39","40","41","42"]
]

current_piece = "R", "Y"

def print_grid():
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if col != 2:
                print(grid[row][col], end="  ")            
            else:
                print(grid[row][col])
                print()

def is_bad_choice_string(choice : str):
    if (choice.isnumeric() and int(choice) >= 1 and int(choice) <= 9):
        return False
    return True

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

def place_piece(grid_spot : int):
    while(True):
        row = get_row(grid_spot)
        col = get_col(grid_spot)
        grid_value = grid[row][col]
        if (not grid_value.__eq__("R") and not grid_value.__eq__("Y")):
            break
        user_choice = ""
        while (is_bad_choice_string(user_choice)):
            user_choice = input(
                "Enter a number (1-42) where to put the piece: ")
        grid_spot = int(user_choice)
    grid[row][col] = current_piece 

def check_row():
    for row in range(4):
        if grid[row][0].__eq__(grid[row][1]) and grid[row][1].__eq__(grid[row][2]):
            return True
    return False

def check_col():
    for col in range(4):
        if grid[0][col].__eq__(grid[1][col]) and grid[1][col].__eq__(grid[2][col]):
            return True
    return False

def check_left_diag():
    return grid[0][0].__eq__(grid[1][1]) and grid[1][1].__eq__(grid[2][2])

def check_right_diag():
    return grid[0][2].__eq__(grid[1][1]) and grid[1][1].__eq__(grid[2][0])

def check_draw():
    for row in range(4):
        for col in range(4):
            if grid[row][col].isnumeric():
                return False  
    return True

def check_game_over():
    if check_row():
        print(current_piece + " wins!")
        return True
    elif check_col():
        print(current_piece + " wins!")
        return True
    elif check_left_diag():
        print(current_piece + " wins!")
        return True
    elif check_right_diag():
        print(current_piece + " wins!")
        return True
    elif check_draw():
        print("The Game Ends in a Draw!")
        return True
    else:
        return False

def game_loop():
    global current_piece
    print("Welcome to TIC TAC TOE")
    user_choice = ""
    while(True):
        print_grid()
        while(is_bad_choice_string(user_choice)):
            user_choice = input("Enter STOP to end.  Or a number (1-9) where to put the piece: ")
        if user_choice.__eq__("STOP"):
            break
        grid_spot = int(user_choice)
        place_piece(grid_spot)
        if(check_game_over()):
            print_grid()
            break
        current_piece = "Y" if current_piece.__eq__("R") else "R"
        user_choice = ""
    print("GAME OVER")

def game_loop():
    global current_piece
    print("LET'S PLAY CONNECT 4!")
    user_choice = ""
    while(True):
        print_grid()
        while((user_choice)):
            user_choice = input("Enter STOP to end.  Or a number (1 - 42) where to put the piece: ")
        if user_choice.__eq__("STOP"):
            break
        grid_spot = int(user_choice)
        place_piece(grid_spot)
        if(check_game_over()):
            print_grid()
            break
        current_piece = "Y" if current_piece.__eq__("R") else "R"
        user_choice = ""
    print("GAME OVER")

game_loop()          