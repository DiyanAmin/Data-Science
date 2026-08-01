from pathlib import Path
print('[IMPORT] Imported Path from pathlib')

path = Path(r'C:\Users\Admin\OneDrive\Desktop\Coding\Data Science\Machine Learning\Machine Learning 2\Logistic Regression\funcs.py')
with open(path,'r') as f:
    exec(f.read())

import pandas as pd
import_('Imported pandas as pd')#type:ignore
from matplotlib import pyplot as plt
import_('Imported pyplot as plt from matplotlib')#type:ignore
from sklearn.model_selection import train_test_split
import_('Imported traim_test_split() from sklearn.model_selection') #type:ignore
from sklearn.linear_model import LogisticRegression
import_('Imported LogisticRegression from sklearn.linear_model') # type:ignore
import math as m
import_('Imported math as m')#type:ignore

df = pd.read_csv('insurance_data.csv')
print(df.head())

# Show column names to confirm
print(df.columns.tolist())

# Strip whitespace and normalize casing
df.columns = df.columns.str.strip().str.lower()

plt.scatter(df['age'],df['bought_insurance'],marker='+',color='red')
plt.show()

x_train,x_test,y_train,y_test = train_test_split(df[['age']],df['bought_insurance'],train_size=0.8)

output(f'x_test:\n{x_test}\n')#type:ignore

model = LogisticRegression()
model.fit(x_train,y_train)

output(f'x_test:\n{x_test}\n')#type:ignore

y_pred = model.predict(x_test)

output(f'Probability of x_test:\n{model.predict_proba(x_test)}')#type:ignore

output(f'Score: {model.score(x_test,y_test)}')#type:ignore

output(f'y_pred:\n{y_pred}')#type:ignore

output(f'x_test:\n{x_test}\n')#type:ignore

output(f'Co-efficient:\n{model.coef_}\n')#type:ignore

output(f'Intercept:\n{model.intercept_}\n')#type:ignore

def pred_func(age:float):
    return 1/(1+m.exp(-(0.042150133 * age - 1.52726963)))

output(f'Age is 35: {pred_func(35)}') #type:ignore

output(f'Age is 43: {pred_func(43)}') #type:ignore