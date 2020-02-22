'''
lecture1_example10.py. This module imports webdriver from selenium. 
It then creates a headless browser using PhantomJS() and searches
for "python" on Google. Finally, it prints the driver's current url 
and quits the driver.
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.PhantomJS()
driver.set_window_size(1200, 600)
driver.get("https://www.google.com/")
driver.find_element_by_name("q").send_keys("python")
driver.find_element_by_name("q").send_keys(Keys.RETURN)
print driver.current_url
driver.quit()