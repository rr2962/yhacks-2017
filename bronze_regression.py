# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 03:02:13 2017

@author: udainagpal
"""

# Import required packages
import numpy as np
import pandas as pd
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt

data_tr = pd.read_csv("FullDatasetVitech.csv", dtype=str, sep=',', index_col=0)
x_tr = data_tr.values[:, 4:].astype(float)
y_tr = data_tr.values[:,2].astype(float)
feat_tr = data_tr.columns[1:].values.astype(str)
samp_tr = data_tr.index.values.astype(str)

#Data Partitioning
X_train, X_test, y_train, y_test = train_test_split(x_tr, y_tr, test_size=0.25, random_state=0)

#Training for random forest regression
clf = RandomForestRegressor (n_estimators=500, random_state=0)
clf.fit(X_train, y_train)
ranking = np.argsort(clf.feature_importances_)[::-1]

bronze_premium = clf.predict(INPUT_DATA)