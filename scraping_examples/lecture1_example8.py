'''
lecture1_example8.py. This module imports urlopen from urllib2,
BeautifulSoup from bs4, and re. It then uses a GET request to pull the source
code for the "commodity" page on Wikipedia. It first prints the set of all
links. It then passes a regular expression to BeautifulSoup to extract
only the links that point to internal Wikipedia articles.
'''

from urllib2 import urlopen
from bs4 import BeautifulSoup
import re

url = "https://en.wikipedia.org/wiki/Commodity"
html = urlopen(url)
soup = BeautifulSoup(html.read())
for link in soup.findAll("a"):
	if "href" in link.attrs:
		print(link.attrs["href"])
		
for link in soup.find("div", {"id":"bodyContent"}).findAll("a", href=re.compile("ˆ(/wiki/)((?!:).)*$")):
	if "href" in link.attrs:
		print(link.attrs["href"])
		
		