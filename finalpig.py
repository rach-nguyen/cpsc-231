import random
import sys
import stdio

def comp(total_comp):
    turn_score_comp=0
    while turn_score_comp<20:
        a=random.randrange(1,7)
        turn_score_comp+=a
        print("Rolled a ", a)
        if a==1:
            turn_score_comp=0
            print("Pig out")
            break
    total_comp+=turn_score_comp
    print("Turn score:", turn_score_comp)
    print("Computer score:", total_comp)
    return total_comp

total_comp=0
turn_score_comp=0
total_play1=0
turn_score1=0

c=random.randrange(0,2)

if c==0:
    print("Computer's turn")
    total_comp=comp(total_comp)


while total_play1<100 and total_comp<100:

    print("Would you like to roll or hold? Input 'r' for roll or 'h' for hold." )

    stuff_typed=stdio.readString()

    if stuff_typed=="r":
        b=random.randrange(1,7)
        print("Rolled a ", b)
        turn_score1+=b
        if b==1:
            turn_score1=0
            print("Pig out!")

    if total_play1>=100 or total_comp>=100:
        break

    if stuff_typed=="h" or b==1:
        if stuff_typed=="h":
            total_play1+=turn_score1
            turn_score1=0
        print("Player 1 score:", total_play1)
        print("Computer's turn")
        total_comp=comp(total_comp)

if total_play1>=100 and total_comp<100:
    print(total_play1,"vs", total_comp)
    print("Congratulations! Player 1 wins!")
else:
    print(total_play1,"vs", total_comp)
    print("Sorry Computer beat you!")