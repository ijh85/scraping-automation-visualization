'''
lecture3_example7.py. This example downloads all monthly reports from wool.com,
computes sentiment scores using the McDonald-Loughran (2011) method, and then
generates a dynamic plot in Bokeh to render the results.
'''

import os
from urllib2 import urlopen
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords
import PyPDF2
import re
import time
import pysentiment as ps
import pandas as pd
import numpy as np
from math import pi
from bokeh.io import show
from bokeh.plotting import figure
from bokeh.models import (
    ColumnDataSource,
    HoverTool,
    LinearColorMapper,
    BasicTicker,
    PrintfTickFormatter,
    ColorBar,
)

# Set save directory.

save_dir = '..'

# Set urls.

url = 'https://www.wool.com'
url0 = 'https://www.wool.com/market-intelligence/monthly-market-reports/?page=1&month='
url1 = '&year='

# Define lists.

links = []
lmonths = []
lyears = []
months = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
years = ['2013', '2014', '2015', '2016', '2017']

# Get links to reports.

for year in years:
	for month in months:
		html = urlopen(url0+month+url1+year).read()
		soup = BeautifulSoup(html)
		link = soup.findAll("a", {"class":"btnPrimary"})
		if(len(link)>0):
			links.append(link)
		else:
			links.append('')
		lmonths.append(month)
		lyears.append(year)
		print month, year
		time.sleep(3)
	
# Extract links.

for j in range(len(links)):
	try:
		links[j] = url+links[j][0]['href']
	except:
		links[j] = ''

# Define sentiment model.

lm = ps.LM()

# Load, save, and delete pdf.

def load_and_process_pdf(link):
	content = urlopen(link).read()
	with open(save_dir+'content.pdf', 'wb') as f:
		f.write(content)
	time.sleep(5)
	content = PyPDF2.PdfFileReader(open(save_dir+'content.pdf'), "rb")
	content_text = [content.getPage(j).extractText() for j in range(content.numPages)]
	content_text = ' '.join(content_text)
	os.unlink(save_dir+'content.pdf')
	return content_text

# Compute sentiment scores.

def compute_sentiment_scores(link):
	try:
		page = load_and_process_pdf(link)
		processed_page = lm.tokenize(page)
		sentiment = lm.get_score(processed_page)
		negativity = sentiment['Negative']
		polarity = sentiment['Polarity']
		positivity = sentiment['Positive']
		subjectivity = sentiment['Subjectivity']
	except:
		sentiment = ''
		negativity = ''
		polarity = ''
		positivity = ''
		subjectivity = ''
	return negativity, polarity, positivity, subjectivity

# Run main loop.

sent = []

for link in links:
	sent.append(compute_sentiment_scores(link))
	print link

# Extract sentiment scores.

negativity = [x[0] for x in sent]
polarity = [x[1] for x in sent]
positivity = [x[2] for x in sent]
subjectivity = [x[3] for x in sent]

# Arrange polarity into date array.

Jan = polarity[0::12]
Feb = polarity[1::12]
Mar = polarity[2::12]
Apr = polarity[3::12]
May = polarity[4::12]
Jun = polarity[5::12]
Jul = polarity[6::12]
Aug = polarity[7::12]
Sep = polarity[8::12]
Oct = polarity[9::12]
Nov = polarity[10::12]
Dec = polarity[11::12]

# Rearrange data to match Bokeh plot formatting.

data = pd.DataFrame(np.vstack([Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec]).T,\
	columns=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
data = data.apply(lambda x: x.str.strip()).replace('', np.nan).astype('float')
data = data.set_index([['2013', '2014', '2015', '2016', '2017']])
data.index.name = 'Year'
data.columns.name = 'Month'
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Plot data.

df = pd.DataFrame(data.stack(), columns=['Sentiment']).reset_index()

colors = ["#550b1d", "#933b41", "#cc7878", "#ddb7b1", "#dfccce", "#e2e2e2", "#c9d9d3", "#a5bab7", "#75968f"]

mapper = LinearColorMapper(palette=colors, low=df.Sentiment.min(), high=df.Sentiment.max())

source = ColumnDataSource(df)

TOOLS = "hover,save,pan,box_zoom,reset,wheel_zoom"

p = figure(title="Wool Sentiment Score ({0} - {1})".format(years[0], years[-1]),
           x_range=years, y_range=list(reversed(months)),
           x_axis_location="above", plot_width=400, plot_height=400,
           tools=TOOLS, toolbar_location='below')

p.grid.grid_line_color = None
p.axis.axis_line_color = None
p.axis.major_tick_line_color = None
p.axis.major_label_text_font_size = "5pt"
p.axis.major_label_standoff = 0
p.xaxis.major_label_orientation = pi / 3

p.rect(x="Year", y="Month", width=1, height=1,
       source=source,
       fill_color={'field': 'Sentiment', 'transform': mapper},
       line_color=None)

p.select_one(HoverTool).tooltips = [
     ('date', '@Month @Year'),
     ('Sentiment', '@Sentiment'),
]

show(p)