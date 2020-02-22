'''
lecture1_example5.py. This module imports urlopen from urllib2 and 
BeautifulSoup from bs4. It then sends a GET request to 
https://online.auktionsverket.com/ and converts the resulting 
HTML into a BeautifulSoup object. The rest of the file demonstrates
basic navigational options for a BeautifulSoup parse. 
'''

from urllib2 import urlopen
from bs4 import BeautifulSoup

url = "https://online.auktionsverket.com/"
html = urlopen(url)
soup = BeautifulSoup(html.read())
soup.title
soup.title.name
soup.title.string
soup.title.parent.name
soup.p
soup.a
soup.find_all('a')
links = soup.find_all('a')
for link in links[0:5]:
	print link

