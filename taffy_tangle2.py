import stddraw
import stdarray
import random
import taffydraw
import time

looking_for_board = True
game_start = time.time()
#array that contains numbers that corresponds to taffies
array = stdarray.create2D(9,7,0.0)

def generate_board():
    #initial board
    stddraw.clear()
    for i in range(len(array)):
        for j in range(7):
            a = random.randrange(1,7)
            array[i][j] = a
            y = -i + 1-1.5
            x = j + 1-0.5
            if a == 1:
                taffydraw.pika(x,y)
            if a == 2:
                taffydraw.guy(x,y)
            if a == 3:
                taffydraw.sonny(x,y)
            if a == 4:
                taffydraw.dog(x,y)
            if a == 5:
                taffydraw.roblox(x,y)
            if a == 6:
                taffydraw.trash(x,y)

def get_index(x,y):
    #gets index of mouse click
    xn=((x-0)/(7-0))
    yn=-((y-0)/(9-0))
    cw=1/7
    rw=1/9
    c = int(xn/cw)
    r = int(yn/rw)
    return r,c

#horizontal
def swap_horizontal(array,yes_match,score,remove_matches,drop_taffies):
        for i in range(9):
            for j in range(6):
                if int(x) < int(x2):
                    #first click less than second click
                    #first click is to the left of second click
                    temp = array[i][j]
                    array[i][j] = array[i][j+1]
                    array[i][j+1]= temp
            #check if match is made
            if yes_match() == True:
                #if a match is made add to score, remove matches and fill space
                score +=100
                remove_matches()
                drop_taffies()
            else:
                #no match, reverts the swap
                temp = array[i][j+1]
                array[i][j+1] = array[i][j]
                array[i][j] = temp

        #first click greater than second click
        for i in range(9):
            for j in range(8):
                if int(x) > int(x2):
                    temp = array[i][j]
                    array[i][j] = array[i][j-1]
                    array[i][j-1] = temp
            if yes_match() == True:
                score +=100
                remove_matches()
                drop_taffies()
            else:
                temp = array[i][j-1]
                array[i][j-1] = array[i][j]
                array[i][j] = temp

def swap_vertical(array,yes_match,score,remove_matches,fill_holes):
        for i in range(8):
            for j in range(7):
                if int(y) > int(y2):
                    temp = array[i][j]
                    array[i][j] = array[i+1][j]
                    array[i+1][j] = temp
        for i in range(10):
            for j in range(7):
                if int(y) < int(y2):
                    temp = array[i][j]
                    array[i][j] = array[i-1][j]
                    array[i-1][j] = temp


def yes_match():
    for i in range(len(array)-2):
        for j in range(len(array[i])-2):
            #checks rows for 3 in a row
            if array[i][j] == array[i][j+1] == array[i][j+2]:
                return True
            #checks columns for 3 in a row
            elif array[i][j] == array[i+1][j] == array[i+2][j]:
                return True
    return False

def remove_matches():
    #changes index into a 0
    for i in range(len(array)-2):
        for j in range(len(array[i])-2):
            if array[i][j] == array[i][j+1] == array[i][j+2]:
                array[i][j] = 0
                array[i][j+1] = 0
                array[i][j+2] = 0
            if array[i][j] == array[i+1][j] == array[i+2][j]:
                array[i][j] = 0
                array[i+1][j] = 0
                array[i+2][j]= 0

def fill_holes():
    #only fills holes in initial board set up
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == 0:
                #if theres a 0 then fill it with new random
                a = random.randrange(1,7)
                array[i][j]=a
                y = -i + 1-1.5
                x = j + 1-0.5
                if a == 1:
                    taffydraw.pika(x,y)
                if a == 2:
                    taffydraw.guy(x,y)
                if a == 3:
                    taffydraw.sonny(x,y)
                if a == 4:
                    taffydraw.dog(x,y)
                if a == 5:
                    taffydraw.roblox(x,y)
                if a == 6:
                    taffydraw.trash(x,y)

def draw_blanks():
    new_array = array
    for i in range(len(new_array)):
        for j in range(len(new_array[i])):
            y=-i+1-1.5
            x=j+1-.5
            if new_array[i][j]==0:
                stddraw.setPenColor(stddraw.WHITE)
                stddraw.filledSquare(x,y,0.5)

def drop_taffies():
    #drops taffies into holes
    while '0' in array:
    #while there are still holes
        for i in range(8):
            for j in range(7):
                if array[i][j] == 0:
                    #checks for blanks
                    array[i+1][j] = array[i][j]
                    array[i][j] = array[i+1][j]
                    array[i+1][j] = temp
                    # swaps with the one above it

first_click = None
click = 1
score = 0
arr1 = []
arr2 = []
new_array = []
score = 0

#global code
taffydraw.configuration()
#game loop
while looking_for_board:
    generate_board()
    print(array)
    stddraw.show(1000)
    remove_matches()
    stddraw.show(1000)
    print(array)
    draw_blanks()
    stddraw.show(1000)
    fill_holes()
    stddraw.show(1000)
    looking_for_board = False

while not looking_for_board:
    taffydraw.draw_clock(game_start)
    #if time runs out then game ends
    taffydraw.score(score)
    taffydraw.goal()
    if stddraw.mousePressed():
        click*=-1
        if click == -1:
            x = stddraw.mouseX()
            y = stddraw.mouseY()
            #get x and y coords from first mouse click
            if x <=7:
                taffydraw.box(int(x)+.5,int(y)-.5)
                #draws selection box
                get_index(x,y)
                #gets index of click
        if click == 1:
            #second click
            x2 = int(stddraw.mouseX())
            y2 = int(stddraw.mouseY())
            get_index(x2,y2)
            adjacent = int(abs((x-x2) + (y-y2)))
            yes_a = True
            if adjacent == 1:
                yes_a = True
                #yes its adjacent
            else:
                yes_a = False
            if yes_a == False:
                #unselect box
                taffydraw.clear_box(int(x)+.5,int(y)-.5)
            else:
                #do swaps & matches
                swap_horizontal(array,yes_match,score,remove_matches,drop_taffies)
                swap_vertical(array,yes_match,score,remove_matches,drop_taffies)
                print(array)
        if score == 1000:
            taffydraw.win()

    stddraw.show(1000)
