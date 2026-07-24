from matplotlib import pyplot as plt
print('[IMPORT] matplotlib.pyplot')
import pandas as pd
print('[IMPORT] pandas')
import numpy as np
print('[IMPORT] numpy')
import seaborn as sb
print('[IMPORT] seaborn')
from sklearn import datasets, linear_model
print('[IMPORT] datasets and linear_model')
from sklearn.metrics import mean_squared_error, r2_score
print('[IMPORT] mean_squared_error , r2_score\n')

data = pd.read_csv('xydataset.csv')

print(data.isnull().any())

data= data.iloc[:,1:]
data.columns = ['X','Y']

x = data[['X']]
y = data[['Y']]

mod = linear_model.LinearRegression()
mod.fit(x,y)

yPred = mod.predict(x)

print(f'[OUTPUT] Coefficient: {mod.coef_[0]}')
print(f'[OUTPUT] Intercept: {mod.intercept_}')
print(f'[OUTPUT] Mean Squared Error: {mean_squared_error(y,yPred)}')
print(f'[OUTPUT] R2 Score: {r2_score(y,yPred)}')

plt.figure(figsize=(10,6))
plt.plot(data['X'],yPred,color='red',label='Regression Line')

plt.ylabel('Y')
plt.xlabel('X')

plt.title('Linear Regression')
plt.legend()
plt.show()

