'''
lecture1_example9.py. This module imports urlopen from urllib2,
BeautifulSoup from bs4, re, random, and time. It provides the
baseline code for a crawler that identifies all links on a page,
randomly visits one, and repeats the process until it arrives
at a page with no outbound links.
'''

from urllib2 import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import time
import re

html = urlopen("https://en.wikipedia.org")
soup = BeautifulSoup(html.read())
links = soup.find("div", {"id":"bodyContent"}).\
findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))

while len(links) > 0:
	link = links[random.randint(0, len(links)-1)].\
	attrs["href"]
	print(link)
	html = urlopen("https://en.wikipedia.org/"+link)
	soup = BeautifulSoup(html.read())
	links = soup.find("div", {"id":"bodyContent"}).\
	findAll("a", href = re.compile("^(/wiki/)((?!:).)*$"))
	time.sleep(5)
		
		