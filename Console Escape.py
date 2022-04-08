import time
map = [["#","#","#","E","#"],
       ["#","#","#",".","#"],
       ["#",".",".",".","#"],
       ["#",".","#","#","#"],
       ["#",".","#","#","#"]]

playerX = 4
playerY = 1
lose = True

player_position = "P"

map[playerX][playerY] = player_position

def create_map(map):
    for x in map:
        for y in x:
            print(y, end=' ')
        print()

def slow_print(str):
  for char in str:
    print(char, end='',flush=True)
    time.sleep(0.01)

def main():
    global playerX,playerY,lose
    slow_print("Welcome to Console Escape!\n")
    slow_print("1) Play Game\n")
    slow_print("2) Quit Game\n")

    start = input("Choose one please!: ")

    if "1" in start:
        while lose:
            create_map(map) 
            slow_print("Up: W\nDown: S\nLeft: A\nRight: D\n")
            dirc = input("Please input a direction ")
            slow_print("---------------------------\n")
            if dirc == "w":
                if map[playerX - 1][playerY] != "#":
                    map[playerX][playerY] = "."
                    playerX -= 1
                    map[playerX][playerY] = "P"
            if dirc == "a":
                if map[playerX][playerY - 1] != "#":
                    map[playerX][playerY] = '.'
                    playerY -= 1
                    map[playerX][playerY] = "P"
            if dirc == "s":
                if map[playerX + 1][playerY] != "#":
                    map[playerX][playerY] = "."
                    playerX += 1
                    map[playerX][playerY] = "P"
            if dirc == "d":
                if map[playerX][playerY + 1] != "#":
                    map[playerX][playerY] = '.'
                    playerY += 1
                    map[playerX][playerY] = "P"
    
            if playerX == 0 and playerY == 3:
                lose = False
                slow_print("You Made it to the end of the maze")
    if "2" in start:
        slow_print("Wow . . . Okay, Fine, Dont Play the game I put time and effort into. . . . . . Jerk :(\n")
main()

