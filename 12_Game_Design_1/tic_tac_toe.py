grid = [
    ["-","-","-"],
    ["-","-","-"],
    ["-","-","-"]
]

#Prints game grid
def print_grid():
    for number in range(len(grid)):
        print(grid[number][0], end="")
        print("|", end="")
        print(grid[number][1], end="")
        print("|", end="")
        print(grid[number][2])
        if (number !=2):
               print("*****")
            
#Prints inro to game
def game_intro():
    print("Welcom to TIC-TAC-TOE!!")

#Game Loop
def game_loop():

    game_intro()

    while(True):
        user_request = input("Enter STOP to end the game, or anything else to continue.")
        if user_request.__eq__("STOP"):
            break
        print("loop running!")
    
    print("Game Over")

game_loop()
