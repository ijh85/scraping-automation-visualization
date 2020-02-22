'''
lecture2_example6.py. This example imports the threading and time modules. It 
then demonstrates how threads can be used to schedule tasks that are not 
executed sequentially.
'''

import threading
import time

def doSomething():
	for j in range(100):
		time.sleep(1)
		print('Something.')
	
def doSomethingElse():
	for j in range(100):
		time.sleep(1)
		print('Something else.')

thread1 = threading.Thread(target=doSomething()).start()
thread2	= threading.Thread(target=doSomethingElse()).start()
	