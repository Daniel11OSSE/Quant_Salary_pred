# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 17:05:28 2020

@author: Dani Ossé
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('C:/Users/ossed/MyDSProjects/Quant_salary_prediction/Quant_salary_prediction/data_eda.csv')

#choose relevant columns
df.columns

df_model = df[['avg_salary','Rating','Size','Type of ownership','Industry','Sector','Revenue','hourly','job_state','age','python_yn', 'R_yn', 'spark', 'aws', 'excel', 'mathematics', 'finance','modeling', 'C++', 'portfolio_theory','derivatives', 'trading', 'sql','job_simp','seniority','desc_len']]
#df_model = df[['avg_salary','Rating','Size','Type of ownership','Industry','Sector','Revenue','hourly','job_state','age','job_simp','seniority','desc_len']]

# get dummy data
df_dum = pd.get_dummies(df_model)

# train test split
from sklearn.model_selection import train_test_split

X = df_dum.drop('avg_salary', axis = 1)
y = df_dum.avg_salary.values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)

# support vector machine regressor
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVR

param_grid = [{'kernel' : ["linear"], 'C':[1,10,100,1000]},{'kernel' : ["rbf"], 'C':[1,10,100,1000], 'gamma' : [1e-3, 1e-4, 0.0005]},]

svr_reg = SVR()

grid_svr = GridSearchCV(svr_reg, param_grid, cv=3,scoring = 'neg_mean_squared_error',return_train_score=True)
grid_svr.fit(X_train, y_train)

grid_svr.best_score_
grid_svr.best_estimator_

# Decision Tree Regressor
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeRegressor
tree_reg = DecisionTreeRegressor()
tree_reg.fit(X_train, y_train)
np.mean(cross_val_score(tree_reg, X_train, y_train, scoring = 'neg_mean_absolute_error', cv = 3))
#-43.635846078711644

# Random forest
from sklearn.ensemble import RandomForestRegressor
rf = RandomForestRegressor()
np.mean(cross_val_score(rf, X_train, y_train, scoring = 'neg_mean_absolute_error', cv = 3))
#-38.921721559144906

# Fine-tuning with Grid Search for RandomForestRegressor
parameters = {'n_estimators':range(10,300,10), 'criterion':('mse','mae'), 'max_features':('auto','sqrt','log2')}

gs = GridSearchCV(rf,parameters,scoring='neg_mean_absolute_error',cv=3)
gs.fit(X_train,y_train)

gs.best_score_
#-37.182269595495626
gs.best_estimator_

# test ensembles 
tpred_svr = grid_svr.best_estimator_.predict(X_test)
tpred_tree = tree_reg.predict(X_test)
tpred_rf = gs.best_estimator_.predict(X_test)

from sklearn.metrics import mean_absolute_error
mean_absolute_error(y_test,tpred_svr) #32.81817689644238
mean_absolute_error(y_test,tpred_tree) #44.24610552763819
mean_absolute_error(y_test,tpred_rf) #36.27610848359445

mean_absolute_error(y_test,(tpred_svr+tpred_rf)/2) #34.39544023465382


import pickle
pickl = {'model': gs.best_estimator_}
pickle.dump( pickl, open( 'model_file' + ".p", "wb" ) )

file_name = "model_file.p"
with open(file_name, 'rb') as pickled:
    data = pickle.load(pickled)
    model = data['model']

model.predict(np.array(list(X_test.iloc[1,:])).reshape(1,-1))[0]

list(X_test.iloc[1,:])

