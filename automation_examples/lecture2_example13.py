'''
lecture3_example13.py. Import numpy as np, datetime, and Pushbullet from
pushbullet. Enter you API credentials, capture the current date-time string,
check the validity of your scrape, and then set your scrape status as the
title of oyur message. Use push_note() to send your title and body to all
devices connected to your account.
'''

import numpy as np
import datetime
from pushbullet import Pushbullet

# Enter PushBullet credentials.

apiKey	=	'REPLACE_WITH_YOUR_API_KEY'
pb 		= 	Pushbullet(apiKey)

# Construct today's date string.

body = str(datetime.datetime.now())

# Check scrape status.

def checkStatus():
	'''
	Replace code with function that checks the scrape's status.
	'''
	random_number = np.random.rand(1)[0]
	if(random_number<=.5):
		status = 'Scrape status: Succeeded.'
	if(random_number>.5):
		status = 'Scrape status: Failed.'
	return status

title = checkStatus()	
	
# Send status message to all devices.

pb.push_note(title, body)