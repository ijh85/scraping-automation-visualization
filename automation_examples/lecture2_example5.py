'''
lecture2_example5.py. This example first imports the datetime and time 
modules. It then defines a run date for the program and a delay. 
Next, it begins checking whether the date condition is satisfied. It
repeats this call at the frequency specified by the delay. Once the
condition is violated, doSomething() is called.
'''

import datetime
import time

delay = 60
year = 2017
month = 11
day = 4
hour = 10
minute = 0
second = 0

runDate = datetime.datetime(year, month, day, hour, minute, second)

runDate.year
runDate.month
runDate.day
runDate.hour
runDate.minute
runDate.second

def doSomething():
	return

while datetime.datetime.now() < runDate:
	time.sleep(delay)

doSomething()