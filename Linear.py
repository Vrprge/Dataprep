# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 08:27:12 2018

@author: USER
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# missing Value
dataset=pd.read_csv('Salary_Data.csv')
# missing Value
#dataset=pd.read_csv('Data.csv')
x = dataset.iloc[:,0].values
y = dataset.iloc[:,1].values

#sklearn train and test dataset
from sklearn.cross_validation import train_test_split
x_train,x_tst,y_train,y_tst= train_test_split(x , y, test_size=1/3, random_state=0)
from sklearn.linear_model import LinearRegression
lreg = LinearRegression()
lreg.fit(x_train,y_train)

plt.scatter(x_train,y_train,color='black')
plt.show()