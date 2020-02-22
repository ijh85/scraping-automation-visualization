'''
lecture3_example1.py. This example imports the Natural Language Toolkit (nltk)
and the Gutenberg Corpus from nltk.corpus. It then loads Milton's "Paradise 
Lost," performs both sentence and word tokenization on the text, and then
constructs a frequency distribution from the words.
'''

import nltk
from nltk.corpus import gutenberg

nltk.corpus.gutenberg.fileids()
paradise = gutenberg.raw(fileids='milton-paradise.txt')
print len(paradise)
print paradise[:35]

sentenceTokenizer = nltk.sent_tokenize
paradiseSentences = sentenceTokenizer(text=paradise)
print paradiseSentences[500]

wordTokenizer = nltk.word_tokenize
paradiseWords = wordTokenizer(text=paradise)
print len(paradiseWords)
print paradiseWords[150:160]

fdist = nltk.FreqDist(w.lower() for w in paradiseWords)
wlist = ['horse', 'automobile']

for i in wlist:
	print(i + ':', fdist[i])