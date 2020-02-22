'''
lecture1_example7.py. This module imports urlopen from urllib2 and
BeautifulSoup from bs4. It then uses a GET request to pull the source
code for auction listings for books and maps. Next, it passes a 
lambda function to BeautifulSoup to identify the subsest of tags
related to Ireland.  It then uses a regular expression to remove
non-ascii characters and then to extract 1) the time remaining and 2)
the highest bid.
'''

from urllib2 import urlopen
from bs4 import BeautifulSoup
import re

url = "https://online.auktionsverket.com/auktion/Bocker/"
html = urlopen(url)
soup = BeautifulSoup(html.read())
maps = soup.findAll(lambda tag: tag.text.find('IRELAND')>-1)
ireland_map = maps[1].text
print(ireland_map)
ireland_map = re.sub(r'[ˆ\x00-\x7F]+',' ', ireland_map)
re.findall("[0-9]+ hour [0-9]+ minutes", ireland_map)
re.findall("SEK [0-9]+",ireland_map)[1]