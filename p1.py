import sys
import random
import math
import stdarray
import stddraw
import stdstats

array = stdarray.create1D(129,0.0)
variance = 0.05
i = 0
i1= 128

def fill_brownian(array,i,i1,variance,scale):
	#base condtion; when the differences between indexes = 1
	# i.e. theyre next to each other
	if i1-i==1:
		return

	else:
		#find middle index
		mid_index = (i+i1) // 2
		#calculate midpoint value
		avg = (array[i] + array[i1])/2
		#add random number from normal distribution to midpoint value
		delta = random.gauss(0, math.sqrt(variance))
		mp = avg + delta
		#set new variance
		new_var = variance/scale
		#add to array
		array[mid_index] = mp
		#call brownian before midpoint(inclusive)
		fill_brownian(array,i, mid_index,new_var, scale)
		#after midpoint(exclusive)
		fill_brownian(array,mid_index,i1,new_var, scale)
		

def main():

	hurst_ex = float(sys.argv[1])
	scale = 2**(2*hurst_ex)
	fill_brownian(array,i,i1,variance,scale)
	stddraw.setYscale(-1,1)
	stddraw.setXscale(0,len(array))
	stddraw.setPenRadius(0.0)
	stdstats.plotLines(array)
	stddraw.show()

if __name__=='__main__':
	main()

