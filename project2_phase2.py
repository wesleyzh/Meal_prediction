"""
Created on Wed May 5 2016

@author: Weili Zhang
"""

import os.path
import sys
from sklearn.externals import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from pandas import Series, DataFrame
import pandas as pd
from nltk.stem import WordNetLemmatizer
import re
from sklearn.feature_extraction.text import TfidfVectorizer


def search_dishes(ingredients, N, df):
    
    """
    search dishes that match the input ingredients
    
    parameters:
    ingredients: the input ingredients from users
    N: number of dishes
    df: yummly.json data set
    """
    cnt = 1
    for i in range(0, df.shape[0]):
        #check if ingredients have all ingredients required in the meal
        if set(ingredients) > set(df.irow(i)['ingredients']):  
            print 'Meal %d:%d, %s'%(cnt, df.irow(i)['id'],df.irow(i)['ingredients_clean_string'])
            print
            cnt += 1
            if cnt > N:
                break
                
    if cnt < N:
        print "The system does not find enough meals matches your input."
        response  = raw_input("Do you want to see related meals? (Y/N) ")
        
        if response == 'Y':
            for i in range(0, df.shape[0]):
                if set(ingredients) < set(df.irow(i)['ingredients']):  
                    print 'Meal %d:%d, %s'%(cnt, df.irow(i)['id'],df.irow(i)['ingredients_clean_string'])
                    print
                    cnt += 1
                    if cnt > N:
                        break    

method = raw_input("Please enter the classfier 1 (logistic regression) or 2 (random forest): ")

if method == '1':
    if os.path.isfile('yummly_lg.pkl') :
        clf = joblib.load('yummly_lg.pkl')
    else:
        print "yummly_lg.pkl is not existed in the working directory."
        print "Please run logistic_regression.py first."
        sys.exit()
elif method == '2':
    if os.path.isfile('yummly_rf.pkl') :
        clf = joblib.load('yummly_rf.pkl')
    else:
        print "yummly_rf.pkl is not existed in the working directory."
        print "Please run random_forest.py first."
        sys.exit()
else:
    raise ValueError("Classifier must be '1' or '2'; got (%r)"
                             % method)

ingredients =  raw_input("Please enter ingredients seperated by comma: ").decode('utf-8')
#ingredients = "baking powder,eggs,all-purpose flour,raisins,milk,white sugar"
print "Your input ingredients are:"
print ingredients
ingredients = ingredients.split(',')
#ingredients = ['baking powder', ' eggs', ' all-purpose flour', ' raisins', ' milk', ' white sugar']

#to keep the same size of features, read yummly.jsons
traindf = pd.read_json("yummly.json")
traindf['ingredients_clean_string'] = [' , '.join(z).strip() for z in traindf['ingredients']]  
traindf['ingredients_string'] = [' '.join([WordNetLemmatizer().lemmatize(re.sub('[^A-Za-z]', ' ', line)) for line in lists]).strip() for lists in traindf['ingredients']]       


testdf = pd.DataFrame({'ingredients':[]})
testdf['ingredients'] =[ingredients]
testdf['ingredients_clean_string'] = [' , '.join(z).strip() for z in testdf['ingredients']]
testdf['ingredients_string'] = [' '.join([WordNetLemmatizer().lemmatize(re.sub('[^A-Za-z]', ' ', line)) for line in lists]).strip() for lists in testdf['ingredients']]       

corpustr = traindf['ingredients_string']
vectorizertr = TfidfVectorizer(stop_words='english',
                             ngram_range = ( 1 , 1 ),analyzer="word", 
                             max_df = .57 , binary=False , token_pattern=r'\w+' , sublinear_tf=False)
tfidftr=vectorizertr.fit_transform(corpustr).todense()
corpusts = testdf['ingredients_string']
tfidfts=vectorizertr.transform(corpusts).todense()


predictors_ts = tfidfts
print "Predicted cuisine by logistic regression is: %s" % clf.predict(predictors_ts)[0]
print

response = raw_input("Do you want print meals with the ingredients? (Y/N)")
if response == 'Y':
    response = raw_input("How many meals you want to see?")
    dishes = search_dishes(testdf['ingredients'][0], int(response), traindf)
elif response == 'N':
    pass
else:
    raise ValueError("You typed unexpected word (Y/N); got (%r)"% response)    
    