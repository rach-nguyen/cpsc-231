import random

total_score=0
turn_score = 0

while total_score<100:
    while turn_score<20:
        a=random.randrange(1,7)
        print("Rolled a",a)
        turn_score+=a
        if a==1:
            turn_score=0
            print("Pigged out! :(")
            break 
    print("Turn score:", turn_score)
    total_score+=turn_score
    print("Total score:", total_score)
    turn_score=0


print("Your final total is:", total_score)
print("Congrats! You won :~)")