'''
lecture1_example14.py. This module imports urlopen from urllib2, 
multiprocessing.dummy (multithreading), and Pool from multiprocessing
(multiple processes).
'''

from urllib2 import urlopen
from bs4 import BeautifulSoup
from multiprocessing import Pool
import multiprocessing.dummy

# Set threads and processes.

threads = 5
processes = 5

# Set date range.

date_range = range(1980,1985)

# Define pool.

thread_pl = multiprocessing.dummy.Pool(threads)
process_pl = multiprocessing.Pool(processes)

# Define URL opening function.

def url_opener(year):
    html = urlopen("https://www.bls.gov/opub/mlr/"+str(year)).read()
    soup = BeautifulSoup(html)
    links = soup.findAll("a")
    links = [link for link in links if link['href'].find('bls.gov/opub/mlr')>-1]
    return links

# Generate link list using threading.

thread_links = thread_pl.map(url_opener, date_range)
process_links = process_pl.map(url_opener, date_range)

# Flatten.

thread_links = sum(thread_links, [])
process_links = sum(process_links, [])

# Check size of list.

print len(thread_links)
print len(process_links)

# Print sample headlines.

thread_links[:5]
process_links[:5]