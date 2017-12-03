# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 02:55:40 2017

@author: udainagpal
"""

# Import required packages
import numpy as np
import pandas as pd
import sklearn
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt

#Reading in dataset
data_tr = pd.read_csv("FullDatasetVitech.csv", dtype=str, sep=',', index_col=0)
purchased_tr = pd.read_csv("FullDatasetVitech.csv", dtype=str, sep=',', index_col=-1)

#Getting x and y data
x_tr = data_tr.values[:, [0,1,2,3,9,10]].astype(float)
y_tr = purchased_tr.values[:,0].astype(float)
feat_tr = data_tr.columns[1:].values.astype(str)
samp_tr = data_tr.index.values.astype(str)

#Data Partitioning
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x_tr, y_tr, test_size=0.25, random_state=0)

from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier (n_estimators=100, random_state=0)

#Training random forest classifier
clf.fit(X_train, y_train)
ranking = np.argsort(clf.feature_importances_)[::-1]

#Predicting plan from user data
plan_prediction = clf.predict(INSERT INPUT HERE)