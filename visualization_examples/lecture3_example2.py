'''
lecture3_example2.py. This example first imports urlopen from urllib2,
BeautifulSoup from bs4, and nltk. It uses urlopen and BeautifulSoup
to download Janet Yellen's September 26, 2017 speech and parse the
HTML content. It then extracts the text from all paragraph projects, 
cleans them, and computes the frequency with which the word
inflation appears in the speech.
'''

from urllib2 import urlopen
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords

# Download Janet Yellen's speech from September 26, 2017.

url = "https://www.federalreserve.gov/newsevents/speech/yellen20170926a.htm"
html = urlopen(url)
soup = BeautifulSoup(html.read())

# Extract text from all paragraph objects.

paragraphs = soup.findAll('p')
paragraphs = [p.text for p in paragraphs]
len(paragraphs)

# Join the paragraphs into a speech and remove the references section.

speech = ' '.join(paragraphs)
print speech.split('References')[1][0:50]
speech = speech.split('References')[0]

# Tokenize the speech into words.

wordTokenizer = nltk.word_tokenize
wordTokens = wordTokenizer(speech)

# Compute the frequency distribution of word use.

fdist = nltk.FreqDist(wordTokens)

# Count the number of uses of inflation and of all words.

speechLength = len(wordTokens)
inflationCount0 = fdist['inflation']
inflationCount1 = fdist['Inflation']

# Convert word tokens to lowercase. Recompute frequency distribution.

fdist = nltk.FreqDist(w.lower() for w in wordTokens)

# Recompute inflation use count.

inflationCount = fdist['inflation']

# Compute and print inflation intensity.

inflationIntensity = 100.0*inflationCount/speechLength
print inflationIntensity

# Remove stop words.

stops = set(stopwords.words("english"))
wordTokens = [word for word in wordTokens if word not in stops]
fdist = nltk.FreqDist(w.lower() for w in wordTokens)

print 100.0*fdist['inflation']/len(wordTokens)

