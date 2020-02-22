'''
lecture3_example3.py. This example first imports urlopen from urllib2,
nltk, stopwords from nltk.corpus, PorterStemmer from nltk.stem.porter,
PyPDF2, and re. It then downloads one Federal Reserve Bulletin from the
period prior to the Black Tuesday crash (September 1929) and one immediately 
afterwards (November 1929).
'''

from urllib2 import urlopen
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import PyPDF2
import re

# Set save directory.

save_dir = '/Users/isaiah/Desktop/'

# Download and save Federal Reserve Bulletins from September and November of 1929.

url_09_29 = "https://fraser.stlouisfed.org/files/docs/publications/FRB/1920s/frb_091929.pdf"
url_11_29 = "https://fraser.stlouisfed.org/files/docs/publications/FRB/1920s/frb_111929.pdf"

content_09_29 = urlopen(url_09_29).read()
content_11_29 = urlopen(url_11_29).read()

with open(save_dir+'frb_0929.pdf', 'wb') as f:
    f.write(content_09_29)
with open(save_dir+'frb_1129.pdf', 'wb') as f:
    f.write(content_11_29)

# Load downloaded pdfs.

pdf_09_29 = PyPDF2.PdfFileReader(open(save_dir+'frb_0929.pdf'), "rb")
pdf_11_29 = PyPDF2.PdfFileReader(open(save_dir+'frb_1129.pdf'), "rb")

# Extract text from each page and merge across pages.

pdf_09_29_text = [pdf_09_29.getPage(j).extractText() for j in range(pdf_09_29.numPages)]
pdf_11_29_text = [pdf_11_29.getPage(j).extractText() for j in range(pdf_11_29.numPages)]

# Merge pages.

pdf_09_29_text = ' '.join(pdf_09_29_text)
pdf_11_29_text = ' '.join(pdf_11_29_text)

# Remove symbols, numbers, and stopwords.

def tokenize(text):
	text = re.sub('[^A-Za-z]+', ' ', text)
	wordTokens = nltk.word_tokenize(text)
	wordTokens = [token.lower() for token in wordTokens if len(token)>1]
	stops = set(stopwords.words("english"))
	wordTokens = [token for token in wordTokens if token not in stops]	
	return wordTokens
	
tokens_09_29 = tokenize(pdf_09_29_text)
tokens_11_29 = tokenize(pdf_11_29_text)

# Stem tokens.

porter_stemmer = PorterStemmer()

stems_09_29 = [porter_stemmer.stem(token) for token in tokens_09_29]
stems_11_29 = [porter_stemmer.stem(token) for token in tokens_11_29]

# Compute frequency distributions.

fdist_09_29 = nltk.FreqDist(stems_09_29)
fdist_11_29 = nltk.FreqDist(stems_11_29)

# Display most common words.

print fdist_09_29.most_common(5)
print fdist_11_29.most_common(5)

# Add more stopwords.

more_stops = ['june','juli','aug','sep','sept','oct','octob','nov',\
'feder','reserv','nation','cent', 'new', 'year', 'month',\
'per', 'total']

# Recompute frequency distributions.

fdist_09_29 = nltk.FreqDist([stem for stem in stems_09_29 if stem not in more_stops])
fdist_11_29 = nltk.FreqDist([stem for stem in stems_11_29 if stem not in more_stops])