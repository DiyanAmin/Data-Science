import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sb

from sklearn.model_selection import train_test_split as tts
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score as as_

data = pd.read_csv('sample_data.csv',sep=',')
print(data.head())

y = data.pop('TARGET CLASS')
x = data

x_train,x_test,y_train,y_test = tts(x,y,test_size=0.2)

clf_model = DecisionTreeClassifier()
clf_model.fit(x_train,y_train)

y_pred = clf_model.predict(x_test)
print(as_(y_test,y_pred))