import stddraw
import tictacdraw
def wins(score):
    for i in range(3):
        if score[i][0] == score[i][1] == score [i][2] == 1:
            tictacdraw.player_one_win(x,y)
        if score[0][i] == score[1][i] == score [2][i] == 1:
            tictacdraw.player_one_win(x,y)
    for i in range(3):
        if score[i][0] == score[i][1] == score [i][2] ==2:
            tictacdraw.player_two_win(x,y)
        if score[0][i] == score[1][i] == score [2][i] == 2:
            tictacdraw.player_two_win(x,y)
    if score[0][0] == score[1][1] == score[2][2] ==1:
        tictacdraw.player_one_win(x,y)
    if score[0][0] == score[1][1] == score[2][2] ==2:
        tictacdraw.player_two_win(x,y)
    if score[2][0] == score[1][1] == score[0][2] ==1:
        tictacdraw.player_one_win(x,y)
    if score[2][0] == score[1][1] == score[0][2] ==2:
        tictacdraw.player_two_win(x,y)
    return True
def no_win(score):
    for i in range(3):
        if score[i][0] != score[i][1] != score [i][2]:
            tictacdraw.tie_game(x,y)
        if score[0][i] != score[1][i] != score [2][i]:
            tictacdraw.tie_game(x,y)
    if score[0][0] != score[1][1] != score[2][2]:
        tictacdraw.tie_game(x,y)
    if score[2][0] != score[1][1] != score[0][2]:
        tictacdraw.tie_game(x,y)

        return True
play = True
click = 1
score_count = 0
score = [0]*3
for i in range(3):
    score[i] = [0]*3

tictacdraw.draw_board()
tictacdraw.first_turn()

while play:
    mouse_click = stddraw.mousePressed()
    if mouse_click:
        x = stddraw.mouseX()
        y = stddraw.mouseY()
        click *= -1 
        score_count +=1
        if click == -1:
            tictacdraw.X(score, x, y)
            tictacdraw.player_two_turn()
        if click == 1:
            tictacdraw.O(score,x, y)
            tictacdraw.player_one_turn()
        wins(score)
        if score_count == 9:
            no_win(score)
    stddraw.show(1000)