'''
lecture3_example6.py. This example first performs several imports on nltk, re,
numpy, pandas, sklearn, and bokeh. It next imports tweets about Brexit,
cleans them, and applies an LDA topic model. It then identifies which
tweets are associated with which topic. Next, it uses the 
nltk.sentiment.vader library to compute a sentiment score for
each tweet. Finally, it plots the result for each topic using
the Bokeh module.
'''

import nltk
from nltk.corpus import twitter_samples
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import re
import numpy as np
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import NMF, LatentDirichletAllocation
from bokeh.plotting import figure, show, output_file

# Define stemmer.

porter_stemmer = PorterStemmer()
sia = SIA()

# Load tweets

tweets = twitter_samples.strings(twitter_samples.fileids()[-1])

# Clean tweets.

def clean_text(tweet):         
	tweet 	= tweet.strip().lower()
	pattern = "(@[A-Za-z0-9]+)|(#[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|(rt)"      
	cleanedTweet = ' '.join(re.sub(pattern," ",tweet).split())
	wordTokens = nltk.word_tokenize(cleanedTweet)
	wordTokens = [token for token in wordTokens if len(token)>1]
	stops = set(stopwords.words("english"))
	wordTokens = [token for token in wordTokens if token not in stops]
	stemmedTweet = [porter_stemmer.stem(tweet) for tweet in wordTokens]
	cleanedTweet = ' '.join(stemmedTweet)
	return cleanedTweet

# Remove special characters, stopwords, twitter IDs, and hashtags.

cleanedTweets = [clean_text(tweet) for tweet in tweets]

# Train a topic (LDA) model.

lda = LatentDirichletAllocation(n_topics=5, max_iter=5,
                                learning_method='online',
                                learning_offset=50.,
                                random_state=0)

vectorizer = TfidfVectorizer()
tf = vectorizer.fit_transform(cleanedTweets)
feature_names = vectorizer.get_feature_names()
lda.fit(tf)

topic_words = []

for topic in lda.components_:
	word_idx = np.argsort(topic)[::-1][0:1]
	topic_words.append([feature_names[i] for i in word_idx][0])
	
print topic_words

# Construct topic groups.

cameron = [tweet for tweet in cleanedTweets if tweet.find('cameron')>-1]
farage = [tweet for tweet in cleanedTweets if tweet.find('farage')>-1]
claim = [tweet for tweet in cleanedTweets if tweet.find('claim')>-1]
ukip = [tweet for tweet in cleanedTweets if tweet.find('ukip')>-1]
snp = [tweet for tweet in cleanedTweets if tweet.find('snp')>-1]

# Compute tweet sentiment scores.

cameron_compound = [sia.polarity_scores(tweet)['compound'] for tweet in cameron]
farage_compound = [sia.polarity_scores(tweet)['compound'] for tweet in farage]
claim_compound = [sia.polarity_scores(tweet)['compound'] for tweet in claim]
ukip_compound = [sia.polarity_scores(tweet)['compound'] for tweet in ukip]
snp_compound = [sia.polarity_scores(tweet)['compound'] for tweet in snp]

cameron_name= np.array(["cameron"]*len(cameron_compound))
farage_name = np.array(["farage"]*len(farage_compound))
claim_name = np.array(["claim"]*len(claim_compound))
ukip_name = np.array(["ukip"]*len(ukip_compound))
snp_name = np.array(["snp"]*len(snp_compound))

# Plot sentiment.
# Source: https://bokeh.pydata.org/en/latest/docs/gallery/boxplot.html

cats = ["cameron", "claim", "farage", "snp", "ukip"]
compound = np.hstack([cameron_compound, claim_compound, farage_compound, snp_compound, ukip_compound])
name = np.hstack([cameron_name, claim_name, farage_name, snp_name, ukip_name])
df = pd.DataFrame(np.vstack([name, compound]).T, columns=['group', 'score'])
df['score'] = df['score'].astype('float')

# Find the quartiles and IQR for each category

groups = df.groupby('group')
q1 = groups.quantile(q=0.25)
q2 = groups.quantile(q=0.5)
q3 = groups.quantile(q=0.75)
iqr = q3 - q1
upper = q3 + 1.5*iqr
lower = q1 - 1.5*iqr

# Find the outliers for each category

def outliers(group):
    cat = group.name
    return group[(group.score > upper.loc[cat]['score']) | (group.score < lower.loc[cat]['score'])]['score']

out = groups.apply(outliers).dropna()

# Prepare outlier data for plotting.

if not out.empty:
    outx = []
    outy = []
    for cat in cats:
        # only add outliers if they exist
        if not out.loc[cat].empty:
            for value in out[cat]:
                outx.append(cat)
                outy.append(value)

p = figure(tools="save", background_fill_color="#EFE8E2", title="", x_range=cats)

# If no outliers, shrink lengths of stems to be no longer than the minimums or maximums.

qmin = groups.quantile(q=0.00)
qmax = groups.quantile(q=1.00)
upper.score = [min([x,y]) for (x,y) in zip(list(qmax.loc[:,'score']),upper.score)]
lower.score = [max([x,y]) for (x,y) in zip(list(qmin.loc[:,'score']),lower.score)]

# Stems

p.segment(cats, upper.score, cats, q3.score, line_color="black")
p.segment(cats, lower.score, cats, q1.score, line_color="black")

# Boxes

p.vbar(cats, 0.7, q2.score, q3.score, fill_color="#E08E79", line_color="black")
p.vbar(cats, 0.7, q1.score, q2.score, fill_color="#3B8686", line_color="black")

# Whiskers

p.rect(cats, lower.score, 0.2, 0.01, line_color="black")
p.rect(cats, upper.score, 0.2, 0.01, line_color="black")

# Outliers

if not out.empty:
    p.circle(outx, outy, size=6, color="#F38630", fill_alpha=0.6)

p.xgrid.grid_line_color = None
p.ygrid.grid_line_color = "white"
p.grid.grid_line_width = 2
p.xaxis.major_label_text_font_size="12pt"

output_file("brexit_sentiment.html", title="Brexit Sentiment")

show(p)