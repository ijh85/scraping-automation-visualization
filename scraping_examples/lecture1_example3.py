'''
lecture1_example3.py. This module imports urlopen from urllib2 and 
BeautifulSoup from bs4. It sends a get request to 
https://en.wikipedia.org/wiki/Richard_Thaler, extracts the HTML from
the code returned, and then converts it to a BeautifulSoup object.
You can run this code in terminal by navigating to its directory and
then executing the following command: python lecture1_example2.py.
'''

from bs4 import BeautifulSoup
from urllib2 import urlopen

url = "https://en.wikipedia.org/wiki/Richard_Thaler"
html = urlopen(url)
soup = BeautifulSoup(html.read())
print(soup.h1)
print(soup.h1.text)