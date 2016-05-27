
"""
Created on Wed May 5 2016

@author: Weili Zhang
"""



from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import nltk
import re
from nltk.stem import WordNetLemmatizer
from sklearn.svm import LinearSVC
from sklearn.metrics import classification_report
import sklearn.metrics
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import grid_search
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.externals import joblib
import time


#load and format the data
df = pd.read_json("yummly.json")
df['ingredients_clean_string'] = [' , '.join(z).strip() for z in df['ingredients']]  
df['ingredients_string'] = [' '.join([WordNetLemmatizer().lemmatize(re.sub('[^A-Za-z]', ' ', line)) for line in lists]).strip() for lists in df['ingredients']]       


corpustr = df['ingredients_string']
vectorizertr = TfidfVectorizer(stop_words='english', ngram_range = ( 1 , 1 ),analyzer="word", 
                               max_df = .57 , binary=False , token_pattern=r'\w+' , sublinear_tf=False)
tfidftr=vectorizertr.fit_transform(corpustr).todense()
predictors_tr = tfidftr

targets_tr = df['cuisine']  #set response variable


#classifier = LinearSVC(C=0.80, penalty="l2", dual=False)
#parameters = {'C':[1, 10]}
#clf = LinearSVC()
clf = RandomForestClassifier(random_state=1, criterion = 'gini', n_estimators=200)

classifier = clf

print "The random forest model is training..."

start = time.clock()

classifier=classifier.fit(predictors_tr,targets_tr)  #training

print "The training process is completed and the total time is %d seconds" % (time.clock() - start)

predicted =  classifier.predict(predictors_tr)

print "Report of created random forest model:"

print(classification_report(targets_tr, predicted))

joblib.dump(classifier, 'yummly_rf.pkl') 

print "The randomforest model is saved in 'yumly_rf.pkl'"