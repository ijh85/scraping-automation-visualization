'''
lecture1_example6.py. This module imports urlopen from urllib2, 
BeautifulSoup from bs4, and cssselect. It then sends a GET request to 
https://www.hks.harvard.edu/faculty-directory and converts the resulting 
HTML an lxml parse tree. Cssselect is then used to extract and display h2
headings.
'''

from lxml import html
from urllib2 import urlopen
import cssselect

url = "https://www.hks.harvard.edu/faculty-directory"
page = urlopen(url).read()
tree = html.fromstring(page)
h2 = tree.cssselect('h2')
print(h2[5].text_content().strip())
for name in h2[5:-1]:
	print(name.text_content().strip())

