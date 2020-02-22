'''
lecture1_example13.py. This module imports webdriver from selenium
and pandas. It then accesses https://www.rome2rio.com/s/Beijing/Shanghai. 
Next, it uses css selectors to compile a dataset of routes from
Beijing to Shanghai. Finally, it puts the dataset in a pandas
dataframe and exports it to a csv file.
'''

from selenium import webdriver
import numpy as np
import pandas as pd

driver = webdriver.PhantomJS()
driver.set_window_size(1200, 600)
driver.get("https://www.rome2rio.com/s/Beijing/Shanghai")

prices = driver.find_elements_by_css_selector('span.route-summary__price.js-itinerary-price.tip-west')
modes = driver.find_elements_by_css_selector('h2.route-summary__title')
durations = driver.find_elements_by_css_selector('span.route-summary__duration.tip-west')

prices = [price.text for price in prices]
modes = [mode.text for mode in modes]
durations = [duration.text for duration in durations]

data = pd.DataFrame(np.vstack([modes,prices,durations]).T,columns=['Mode','Price','Duration'])
data.to_csv('../Beijing-Shanghai.csv',index=None)