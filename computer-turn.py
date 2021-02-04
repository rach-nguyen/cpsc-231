import random

a=random.randrange(1,7)
sum=0

while sum<20:
    a=random.randrange(1,7)
    print("Rolled a",a)
    sum=sum+a
    if a==1:
        sum=0
        break 

if sum==0:
    print("Pigged out!")

print("Turn score:",sum)

