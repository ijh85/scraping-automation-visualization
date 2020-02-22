'''
lecture2_example4.py. This example first imports the time module. It then 
defines a function that sums the sequence of numbers from (1,X). The 
function is then executed and the runtime is returned.
'''

import time

def calcSum(X):
	s = 0
	for j in range(1,X+1):
		s += j
	return s
	
startTime = time.time()
output = calcSum(10000000)
endTime = time.time()
print endTime-startTime	
