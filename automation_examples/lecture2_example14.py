'''
lecture3_example14.py. The example first imports numpy as np, pandas as pd, 
Pushbullet from pushbullet, time, datetime, and re. It next generates data 
from a random walk for the purpose of illustration. This should be replaced 
with the path to the location of your data in the computeMean() function. 
Next, it extracts the latest push from pushbullet and determines whether 
it 1) happened fewer than 10 minutes ago; and 2) contains two dates. 
If both criteria are satisfied, it computes the series mean between those 
two dates and pushes it to all devices, along with the date range.
'''

import numpy as np
import pandas as pd
from pushbullet import Pushbullet
import time
import datetime
import re

# Generate and save sample data.

def generateRandomWalk():
	days = 10000
	start_date = datetime.datetime.now() + datetime.timedelta(-days)
	datelist = pd.date_range(start_date, periods=days).tolist()
	shocks = np.random.normal(0,1,days)
	randomWalk = np.zeros((days,1))
	randomWalk[0] =	shocks[0]
	for t in range(1,len(randomWalk)):
		randomWalk[t] =	randomWalk[t-1] + shocks[t]
	data = pd.DataFrame(randomWalk,columns=['random_walk'])
	data.index = datelist
	return data
	
data = generateRandomWalk()
data.to_csv('../data.csv')

# Define function to compute mean between selected dates.

def computeMean(dates):
	data = pd.read_csv('../data.csv', index_col=0)
	mean = np.mean(data[dates[0]:dates[1]])[0]
	return mean

# Enter PushBullet credentials.

apiKey	= 'REPLACE_WITH_YOUR_API_KEY'
pb 		= Pushbullet(apiKey)

# Pull the latest push.

latestPush = pb.get_pushes()[0]

# Get Unix time.

unixTime = time.time()

# Get time since latest message sent.

timeSinceLatest = unixTime-latestPush['created']

# Define regular expression.

pattern = re.compile('\d{4}-\d{1,2}-\d{1,2}')

# Check if dates have been pushed within the last 10 minutes.

body = latestPush['body']
dates = re.findall(pattern, latestPush['body'])

if timeSinceLatest<=600 and len(dates)==2:
	mean = computeMean(dates)
	
# Send status message to all devices.

pb.push_note('Mean: '+str(mean), 'Start '+dates[0]+', '+'End '+dates[1])