'''
lecture3_example5.py. This example imports classes from nltk, re,
numpy, and sklearn. It then pulls Reuters articles about corn and 
wheat. The articles are separated into train and tests sets 
and the text is cleaned. We then 1) compute a Tfidf vectorization of
the text corpus; and 2) use the word vectors to estimate a naive bayes
and logistic model. We show that the logistic model performs better
both in and out of sample.
'''

import nltk
from nltk.corpus import reuters
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
import re
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix
from sklearn import linear_model

# Define stemmer.

porter_stemmer = PorterStemmer()

# Load reuters categories.

print reuters.categories()

# Load silver and gold categories.

corn = reuters.fileids(['corn'])
wheat = reuters.fileids(['wheat'])

# Drop common ids.

common = set(corn).intersection(wheat)
corn = [id for id in corn if id not in common]
wheat = [id for id in wheat if id not in common]

# Separate test and train files.

train_corn_ids = [train for train in corn if train.find('train')>-1]
test_corn_ids = [test for test in corn if test.find('test')>-1]

train_wheat_ids = [train for train in wheat if train.find('train')>-1]
test_wheat_ids = [test for test in wheat if test.find('test')>-1]

# Load text data.

train_corn_target = []
test_corn_target = []
train_wheat_target = []
test_wheat_target = []

train_corn = []
test_corn = []
train_wheat = []
test_wheat = []

def load_train_data():
	train = []
	train_target = []
	for id in train_corn_ids:
		train_corn_target.append(0)
		train_corn.append(reuters.raw(id))
	for id in train_wheat_ids:
		train_wheat_target.append(1)
		train_wheat.append(reuters.raw(id))
	train = train_corn + train_wheat
	train_target = train_corn_target + train_wheat_target
	return train, train_target

def load_test_data():
	for id in test_corn_ids:
		test_corn_target.append(0)
		test_corn.append(reuters.raw(id))
	for id in test_wheat_ids:
		test_wheat_target.append(1)
		test_wheat.append(reuters.raw(id))
	test = test_corn + test_wheat
	test_target = test_corn_target + test_wheat_target
	return test, test_target		

train, train_target = load_train_data()
test, test_target = load_test_data()	

# Remove special characters and stopwords, and then stem.

def preprocess_text(text):
	try:
		text = re.sub('[^A-Za-z]+', ' ', text)
		wordTokens = nltk.word_tokenize(text)
		wordTokens = [token.lower() for token in wordTokens if len(token)>1]
		stops = set(stopwords.words("english"))
		wordTokens = [token for token in wordTokens if token not in stops]
		stemmedTokens = [porter_stemmer.stem(token) for token in wordTokens]
		cleanedText = ' '.join(stemmedTokens)
	except:
		cleanedText = ''
	return cleanedText

# Pre-process data.

train = [preprocess_text(doc) for doc in train]
test = [preprocess_text(doc) for doc in test]

# Drop unusable test.

train = [doc for doc in train if len(doc)>0]
test = [doc for doc in test if len(doc)>0]

# Extract features.

vectorizer = TfidfVectorizer()
train_weights = vectorizer.fit_transform(train).toarray()
test_weights = vectorizer.fit_transform(test).toarray()

# Train Naive Bayes classifier.

nb_0 = GaussianNB().fit(train_weights, train_target)

# Predict classification.

train_pred = nb_0.predict(train_weights)

# Confusion matrix.

confusion_matrix(train_target, train_pred)

# Note that we can't do this. We have to vectorize with a common corpus.
#test_pred = nb_0.predict(test_counts)

# Extract features. Use train+test.

weights = vectorizer.fit_transform(np.hstack([train,test])).toarray()
train_weights = weights[:len(train_weights),:]
test_weights = weights[len(train_weights):,:]

# Train Naive Bayes classifier.

nb_1 = GaussianNB().fit(train_weights, train_target)

# Predict train and test set.

train_pred = nb_1.predict(train_weights)
test_pred = nb_1.predict(test_weights)

# Compute confusion matrix.

confusion_matrix(train_target, train_pred)
confusion_matrix(test_target, test_pred)

# Train logistic regression model.

lr = linear_model.LogisticRegression().fit(train_weights, train_target)
train_pred = lr.predict(train_weights)
test_pred = lr.predict(test_weights)

# Compute confusion matrix.

confusion_matrix(train_target, train_pred)
confusion_matrix(test_target, test_pred)
