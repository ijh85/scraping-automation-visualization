'''
lecture3_example4.py. This example first imports nltk, twitter_samples from 
nltk.corpus, stopwords from nltk.corpus, PorterStemmer from nltk.stem.porter,
ngrams from nltk, and re. It then imports a corpus of sample tweets about
Brexit. The tweets are cleaned to remove special characters, hashtags,
and twitter user IDs. The tweet text is then cleaned, tokenized, 
and stemmed. Finally, we compute frequency distributions to try to
determine the most frequently used messages in the tweets. 
'''

import nltk
from nltk.corpus import twitter_samples
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk import ngrams
import re

twitter_samples.fileids()
tweets = twitter_samples.strings(twitter_samples.fileids()[-1])
porter_stemmer = PorterStemmer()

def clean_text(tweet):         
	tweet 	= tweet.strip()   
	pattern = "(@[A-Za-z0-9]+)|(#[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|(RT)"      
	cleaned_tweet = ' '.join(re.sub(pattern," ",tweet).split())
	wordTokens = nltk.word_tokenize(cleaned_tweet)
	wordTokens = [token.lower() for token in wordTokens if len(token)>1]
	stops = set(stopwords.words("english"))
	wordTokens = [token for token in wordTokens if token not in stops]
	cleaned_tweet = ' '.join(wordTokens)
	return cleaned_tweet

# Remove special characters, stopwords, twitter IDs, and hashtags.

cleaned_tweets = [clean_text(tweet) for tweet in tweets]

# Merge.

tweet_corpus = ' '.join(cleaned_tweets)

# Tokenize.

tweet_tokens = nltk.word_tokenize(tweet_corpus)

# Stem tweets.

stemmed_tweets = [porter_stemmer.stem(tweet) for tweet in tweet_tokens]

# Compute frequency.

fdist = nltk.FreqDist(stemmed_tweets)

# Print most common terms.

print fdist.most_common(5)

# Compute 2-gram.

bigram = ngrams(stemmed_tweets, 2)
grams = [gram for gram in bigram]
bifdist = nltk.FreqDist(grams)

print bifdist.most_common(2)

# Compute 3-gram.

trigram = ngrams(stemmed_tweets, 3)
grams = [gram for gram in trigram]
trifdist = nltk.FreqDist(grams)

print trifdist.most_common(2)