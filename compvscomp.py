import random

def player1(total_play1):
    turn_score1=0
    while turn_score1<20:
        a=random.randrange(1,7)
        turn_score1+=a
        print("Rolled a ", a)
        if a==1:
            turn_score1=0
            print("Pig out!")
            break
    total_play1+=turn_score1
    print("Turn score:", turn_score1)
    print("Player 1 score:", total_play1)
    return total_play1

def player2(total_play2):
    turn_score2=0
    while turn_score2<20:
        a=random.randrange(1,7)
        turn_score2+=a
        print("Rolled a", a)
        if a==1:
            turn_score2=0
            print("Pig out!")
            break
    total_play2+=turn_score2
    print("Turn score:", turn_score2)
    print("Player 2 score:", total_play2)
    return total_play2

turn_score1=0
turn_score2=0
total_play2=0
total_play1=0

b=random.randrange(0,2)


while total_play1<100 and total_play2<100:
    if b==0:
        print("Player 1's turn")
        total_play1=player1(total_play1)
    else:
        print("Player 2's turn")
        total_play2=player2(total_play2)
    if total_play1>=100 or total_play2>=100:
        break
    if b==0:
        print("Player 2's turn")
        total_play2=player2(total_play2)
    else:
        print("Player 1's turn")
        total_play1=player1(total_play1)

print(total_play1, "vs", total_play2)
if total_play1>total_play2:
    print("Player 1 wins!")
else:
    print("Player 2 wins!")
