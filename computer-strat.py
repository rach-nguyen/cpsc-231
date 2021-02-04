import random
import sys

number = int(sys.argv[1])
a=random.randrange(1,7)
sum=0
total=a+number
total=0
print("Current score:",number)

while number < 100:
    a=random.randrange(1,7)
    print("rolled a",a)
    sum=sum+a
    total=sum+number
    if a==1:
        sum=0
        total=number
        break
    if total>=100:
        break

if number<100:
    print("Turn score is", sum)
    print("Total score is",total)
else:
    print("Total score is", number)

if sum==0 and number<100:
    print("Pigged out!")
# the Total score should not be 0 if it rolled a 1. 