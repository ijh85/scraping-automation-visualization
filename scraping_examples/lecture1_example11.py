'''
lecture1_example11.py. This module imports webdriver from selenium. 
It then accesses https://www.rome2rio.com/s/Stockholm/Kiev. Finally,
it uses xpath and css selectors to identify all route summaries and then 
prints the route summary header.
'''

from selenium import webdriver

driver = webdriver.PhantomJS()
driver.set_window_size(1200, 600)
driver.get("https://www.rome2rio.com/s/Stockholm/Kiev")

xpath_element = driver.find_element_by_xpath("//*[@id='id5']/div[1]")
print xpath_element.text

css_element = driver.find_element_by_css_selector('div.route-summary__header')
print css_element.text

css_elements = driver.find_elements_by_css_selector('div.route-summary__header')
for element in css_elements:
	print element.text