import sys
import random

number = int(sys.argv[1])
sum = 0

for i in range (number):
	roll = random.randrange(1,7)
	j = 0
	while roll > 1:
		j += 1
		roll = random.randrange(1,7)
	sum+=j
	avg = sum/number
print('Simulate', number,'turns...')
print('Estimated expectation:', avg)