'''
lecture2_example11.py. This example imports modules time, pyautogui,
pandas, numpy, and twilio. It then defines 1) a function to return
the center point of an on screen image; and 2) a function to send SMS
messages to your mobile phone. It then 1) launches a browser, 2) visits
the Treasury Auction site, 3) downloads daily auction data, 4) computes
the mean price, and 5) sends the mean price to your phone via SMS
message.
'''

import time
import pyautogui
import numpy as np
import pandas as pd
from twilio.rest import Client

'''
Define path variables.
'''

downloadPath = '../Downloads/'
imagePath = '../images/'
url = 'https://www.treasurydirect.gov/instit/annceresult/annceresult_query.htm'

'''
Define functions.
'''

def returnCenter(filename, path=imagePath):
	''' 
	Locate an image on screen and return the coordinates of its center.
	'''
	path = imagePath
	location = pyautogui.locateOnScreen(path+filename)
	center = pyautogui.center(location)
	return center

def sendMessage(bodyMessage):
	'''
	Define a function to send SMS messages to your mobile phone.
	'''
	account_sid = "ACXXXXXXXXXXXXXXXXX"
	auth_token = "YYYYYYYYYYYYYYYYYY"
	to_number = "+XXXXXXXXXXXX"
	twilio_number = "+YYYYYYYYYYYY"
	body_message = bodyMessage
	client = Client(account_sid, auth_token)
	client.api.account.messages.create(
		to = to_number,
		from_ = twilio_number,
		body = body_message)

'''
Collect data.
'''

# Open firefox.

firefoxCenter = returnCenter('firefox.png')
pyautogui.moveTo(firefoxCenter, duration=0.25)
pyautogui.doubleClick()

# Wait for firefox to load.

time.sleep(2)

# Load Treasury Auction website.

addressCenter = returnCenter('enter_address.png')
pyautogui.moveTo(addressCenter, duration=0.25)
pyautogui.click()
pyautogui.typewrite(url, interval=0.05)
pyautogui.press('enter')

# Wait for page to load.

time.sleep(3)

# Select the auction date.

dateCenter = returnCenter('auction_date.png')
pyautogui.moveTo(dateCenter, duration=0.25)
pyautogui.moveRel(50, 10)
pyautogui.doubleClick()

# Wait for calendar to load.

time.sleep(2)

# Select today's date.

todayCenter = returnCenter('today.png')
pyautogui.moveTo(todayCenter, duration=0.25)
pyautogui.click()

# Wait for auction list to load.

time.sleep(2)

# Download data in csv format.

csvCenter = returnCenter('csv.png')
pyautogui.moveTo(csvCenter, duration=0.25)
pyautogui.doubleClick()

# Wait for save dialog box.

time.sleep(2)

# Save csv data.

pyautogui.press('enter')

# Load csv data.

data = pd.read_csv(downloadPath+'Securities.csv')

'''
Compute mean price per $100.
'''

try:
	meanPrice = str(np.mean(data['Price per $100']))
except:
	meanPrice = 'No auction data available.'

bodyMessage = 'Price per $100: '+meanPrice+'.'

'''
Send message.
'''

sendMessage(bodyMessage)