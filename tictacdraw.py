import stddraw
import sys
def draw_board():
    stddraw.setPenColor(stddraw.BOOK_LIGHT_BLUE)
    stddraw.line(.375,.125,.375,.875)
    stddraw.line(.625,.125,.625,.875)
    stddraw.line(.125,.375,.875,.375)
    stddraw.line(.125,.625,.875,.625)
def X(score, x, y):
    if x > .625 and x <1:
        if y >.0625 and y < .375:
            stddraw.setPenColor(stddraw.PINK)
            stddraw.setFontSize(76)
            stddraw.text(.75,.25,"X")
            score[2][2] = 1
        if y >.375 and y < .625:
            stddraw.setPenColor(stddraw.PINK)
            stddraw.setFontSize(76)
            stddraw.text(.75,.5,"X")
            score[1][2] = 1
        if y >.625 and y < 1:
            stddraw.setPenColor(stddraw.PINK)
            stddraw.setFontSize(76)
            stddraw.text(.75,.75,"X")
            score[0][2] = 1
    if x >.375 and x <.625:
        if y >.0625 and y <.375:
            stddraw.setPenColor(stddraw.PINK)
            stddraw.setFontSize(76)
            stddraw.text(.5,.25,"X")
            score[2][1] = 1
        if y >.375 and y <.625:
            stddraw.setPenColor(stddraw.PINK)
            stddraw.setFontSize(76)
            stddraw.text(.5,.5,"X")
            score[1][1] = 1
        if y >.625 and y < 1:
            stddraw.setPenColor(stddraw.PINK)
            stddraw.setFontSize(76)
            stddraw.text(.5,.75,"X")
            score[0][1] = 1
    if x >0 and x <.375:
        if y > .0625 and y <0.325:
            stddraw.setPenColor(stddraw.PINK)
            stddraw.setFontSize(76)
            stddraw.text(.25,.25,"X")
            score[2][0] = 1
        if y > .325 and y <.625:
            stddraw.setPenColor(stddraw.PINK)
            stddraw.setFontSize(76)
            stddraw.text(.25,.5,"X")
            score[1][0] = 1
        if y > .625 and y < 1:
            stddraw.setPenColor(stddraw.PINK)
            stddraw.setFontSize(76)
            stddraw.text(.25,.75,"X")
            score[0][0] = 1
def O(score,x,y):
    if x > .625 and x <1:
        if y >.0625 and y < .375:
            stddraw.setPenColor(stddraw.PINK)
            stddraw.setFontSize(76)
            stddraw.text(.75,.25,"O")
            score[2][2] = 2
        if y >.375 and y < .625:
            stddraw.setPenColor(stddraw.PINK)
            stddraw.setFontSize(76)
            stddraw.text(.75,.5,"O")
            score[1][2] = 2
        if y >.625 and y < 1:
            stddraw.setPenColor(stddraw.PINK)
            stddraw.setFontSize(76)
            stddraw.text(.75,.75,"O")
            score[0][2] = 2
    if x >.375 and x <.625:
        if y >0.0625 and y <.375:
            stddraw.setPenColor(stddraw.PINK)
            stddraw.setFontSize(76)
            stddraw.text(.5,.25,"O")
            score[2][1] = 2
        if y >.375 and y <.625:
            stddraw.setPenColor(stddraw.PINK)
            stddraw.setFontSize(76)
            stddraw.text(.5,.5,"O")
            score[1][1] = 2
        if y >.625 and y < 1:
            stddraw.setPenColor(stddraw.PINK)
            stddraw.setFontSize(76)
            stddraw.text(.5,.75,"O")
            score[0][1] = 2
    if x >0 and x <.375:
        if y > .0625 and y <0.325:
            stddraw.setPenColor(stddraw.PINK)
            stddraw.setFontSize(76)
            stddraw.text(.25,.25,"O")
            score[2][0] = 2
        if y > .325 and y <.625:
            stddraw.setPenColor(stddraw.PINK)
            stddraw.setFontSize(76)
            stddraw.text(.25,.5,"O")
            score[1][0] = 2
        if y > .625 and y < 1:
            stddraw.setPenColor(stddraw.PINK)
            stddraw.setFontSize(76)
            stddraw.text(.25,.75,"O")
            score[0][0] = 2
def first_turn():
    stddraw.setFontSize(24)
    stddraw.setPenColor(stddraw.WHITE)
    stddraw.filledRectangle(0,0,1,.09)
    stddraw.setPenColor(stddraw.PINK)
    stddraw.text(0.5,.0625,"Player one goes first! Place your X on the board.")
def player_one_turn():
    stddraw.setFontSize(36)
    stddraw.setPenColor(stddraw.WHITE)
    stddraw.filledRectangle(0,0,1,.09)
    stddraw.setPenColor(stddraw.PINK)
    stddraw.text(0.5,.0625,"It's player one's turn!")
def player_two_turn():
    stddraw.setFontSize(36)
    stddraw.setPenColor(stddraw.WHITE)
    stddraw.filledRectangle(0,0,1,.09)
    stddraw.setPenColor(stddraw.PINK)
    stddraw.text(0.5,.0625,"It's player two's turn!")
def player_one_win(x,y):
    stddraw.setFontSize(36)
    stddraw.setPenColor(stddraw.WHITE)
    stddraw.filledRectangle(0,0,1,.09)
    stddraw.setPenColor(stddraw.PINK)
    stddraw.text(0.5,.0625,"Player one wins!")
    stddraw.setFontSize(24)
    stddraw.text(.8,.0625, "Exit")
    if x>.6 and x <1:
        if y > 0 and y <.125:
            sys.exit()

    stddraw.show(1000)
def player_two_win(x,y):
    stddraw.setFontSize(36)
    stddraw.setPenColor(stddraw.WHITE)
    stddraw.filledRectangle(0,0,1,.09)
    stddraw.setPenColor(stddraw.PINK)
    stddraw.text(0.5,.0625,"Player two wins!")
    stddraw.setFontSize(24)
    stddraw.text(.8,.0625, "Exit")
    if x>.6 and x <1:
        if y > 0 and y <.125:
            sys.exit()

    stddraw.show(1000)
def tie_game(x,y):
    stddraw.setPenColor(stddraw.WHITE)
    stddraw.filledRectangle(0,0,1,.09)
    stddraw.setPenColor(stddraw.PINK)
    stddraw.text(0.5,.0625, "It's a tie!")
    stddraw.text(.8,.0625, "Exit")
    stddraw.setFontSize(24)
    if x>.6 and x <1:
        if y > 0 and y <.125:
            sys.exit()

    stddraw.show(1000)
