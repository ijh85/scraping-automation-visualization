'''
lecture1_example2.py. This module imports BeautifulSoup from the bs4 module.
It then defines a string variable that contains broken HTML code. The string
is converted into a BeautifulSoup object and then prettified using a parser.
'''

from bs4 import BeautifulSoup

broken_html = "<ul class=country><li>Area<li>Area<li>Population</ul>"
soup = BeautifulSoup(broken_html)
fixed_html = soup.prettify()
print(fixed_html)