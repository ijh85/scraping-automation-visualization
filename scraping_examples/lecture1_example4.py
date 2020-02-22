'''
lecture1_example4.py. This module imports urlopen from urllib2 and 
BeautifulSoup from bs4. It sends a GET request to 
http://google.com/404 and receives a 404 error. It then pauses for
60 seconds and attempts the same GET request. If that fails again,
it sends a GET request to a different url.
'''

from bs4 import BeautifulSoup
from urllib2 import urlopen
from urllib2 import HTTPError
import time

url_0 = "http://google.com/404"
url_1 = "http://google.com"

try:
	html = urlopen(url_0)
	soup = BeautifulSoup(html.read())
except HTTPError as e:
	print(e)
	if str(e).find('404')!=-1:
		time.sleep(60)
		try:
			print(e)
			html = urlopen(url_0)
			soup = BeautifulSoup(html.read())
		except HTTPError as e:
			html = urlopen(url_1)
			soup = BeautifulSoup(html.read())
			print('Page found.')

