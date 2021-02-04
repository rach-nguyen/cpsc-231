import sys
import random
prob_else = 5/6
prob6 = (1-(prob_else**6))
prob_other = 5/6
prob12 = ((1-(prob_other**12))-(12*(5**11/6**12)))

print("Estimated likelihood of 1 at least once in 6:", prob6)
print("Estimated likelihood of 1 at least twice in 12:", prob12)
print("Therefore, it is more likely to get a 1 at least once when rolling a die 6 times than getting a 1 at least twice in 12 rolls.")