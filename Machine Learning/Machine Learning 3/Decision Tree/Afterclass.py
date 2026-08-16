from pandas import read_csv as r
import numpy as np
from matplotlib import pyplot as plt

from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split as tts


df = r('Iris Dataset.csv',sep=',')
df.pop('Species')
df.pop('Id')
df.pop('PetalLengthCm')
df.pop('PetalWidthCm')

print(df.head())

x = df['SepalWidthCm']
y = df['SepalLengthCm']


x_train,x_test,y_train,y_test = tts(x,y,test_size=0.2)

model = DecisionTreeClassifier()
model.fit(x_train,y_train)

y_pred = model.predict(x_test)

plt.plot(x=y_test,color='green',label='Real')
plt.plot(x=y_pred,color='red',label='Prediction')

plt.title('Predictions VS Real')

plt.legend()