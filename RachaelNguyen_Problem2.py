import random
import sys

number = int(sys.argv[1])
sum = 0

for i in range(number):
	roll = random.randrange(1,7)
	sum+=roll
	avg = sum/number
	
print('Rolling', number,'times...')
print('Expected value:', avg )