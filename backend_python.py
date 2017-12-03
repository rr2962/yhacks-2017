# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 03:02:13 2017

@author: udainagpal
"""

# Import required packages
import json
from pprint import pprint
import numpy as np
import pandas as pd
import pickle
#import sklearn
#from sklearn.model_selection import train_test_split
#from sklearn.ensemble import RandomForestRegressor
#import matplotlib.pyplot as plt
marital_gender = [“S”, “M”, “F”] 
tobacco = ["No", "Yes"]
states = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin" , "Wyoming", "District of Columbia”]
with open('test.json') as json_data:
    d = json.load(json_data)
    marital_status = marital_gender.index(d['What is your marital status?'])
    age = d['Age']
    sex = d['Sex']
    people_covered = d['How many individuals will be covered?']
    state = states.index(d['State']) + 1
    latitude = d['Latitude']
    longitude = d['Longitude']
    tobacco = tobacco.index(d['Do you smoke or otherwise ingest tobacco or tobacco products?'])
    additional_request = d['Optional: Additional Insurance Requested']
    annual_income = d['What is your annual income?']
#pprint(data)
clfbronze = joblib.load('bronze_regression.pkl')
clfsilver = joblib.load('silver_regression.pkl')
clfgold = joblib.load('gold_regression.pkl')
clfplatinum = joblib.load('platinum_regression.pkl')
clfclassification = joblib.load('classification.pkl')
#Data Partitioning
#X_train, X_test, y_train, y_test = train_test_split(x_tr, y_tr, test_size=0.25, random_state=0)

#Training for random forest regression
#clf = RandomForestRegressor (n_estimators=500, random_state=0)
#clf.fit(X_train, y_train)
bronze_premium = clfbronze.predict([longitude,sex,state,latitude,people_covered,additional_request,annual_income, marital_status,height,weight,tobacco,age])
#ranking = np.argsort(clf.feature_importances_)[::-1]
silver_premium = clfsilver.predict([longitude,sex,state,latitude,people_covered,additional_request,annual_income, marital_status,height,weight,tobacco,age])
gold_premium = clfgold.predict([longitude,sex,state,latitude,people_covered,additional_request,annual_income, marital_status,height,weight,tobacco,age])
platinum_premium = clfplatinum.predict([longitude,sex,state,latitude,people_covered,additional_request,annual_income, marital_status,height,weight,tobacco,age])
#premiums = [bronze_premium, silver_premium, gold_premium, platinum_premium]
premiums = ['dummy', 'bronze', 'silver', 'gold', 'platinum']
type = clfclassification([platinum_premium, gold_premium, bronze_premium, silver_premium, 
            longitude,sex,state,latitude,people_covered,additional_request,annual_income, marital_status,height,weight,tobacco,age])
jstr = '''{
   "WebMessage":{
	“platinum_price” : platinum_premium,
	“gold_price”: gold_premium,
      "silver_price": silver_premium,
	“bronze_price”: bronze_premium,
     "rec_plan": premiums[type],
   }
}'''
j = json.loads(jstr)
jstr = json.dumps(j)
#"""