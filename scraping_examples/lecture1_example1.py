'''
lecture1_example1.py. This module imports urlopen from urllib2. It then sends
a get request to http://www.math.unm.edu/writingHTML/tut/index.html and prints 
the HTML returned. You can execute this script from the command line by 
running python /path_to_directory/lecture1_example1.py from terminal. You 
can also execute the lines of code in an interactive shell, such as iPython 
or Jupyter.
'''

from urllib2 import urlopen

url = "http://www.math.unm.edu/writingHTML/tut/index.html"
html = urlopen(url)
print(html.read())