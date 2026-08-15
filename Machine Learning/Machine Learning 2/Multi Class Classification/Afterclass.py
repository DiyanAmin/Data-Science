def a(string:str,type:bool=True):
    if type:
        print(f'[IMPORT] {string}')
    else:
        print(f'[OUTPU] {string}')

import pandas as pd
a('Imported pandas as pd')

import numpy as np
a('Imported numpy as np')

from matplotlib import pyplot as plt
a('Imported pyplot as plt from matplotlib')

from sklearn.linear_model import LogisticRegression
a('Imported LogisticRegression from sklearn.linear_model')

from sklearn.model_selection import train_test_split as tts
a('Imported train_test_split() as tts() from sklearn.model_selection')

from sklearn.metrics import accuracy_score,classification_report,confusion_matrix
a('Imported accuracy_score(), classification_report() and confusion_matrix() from sklearn.metrics')

df = pd.read_csv('new_name_of_ds.csv')

features = ['Por','Brittle','Perm','TOC']
target = 'Prod'
df = df.dropna(subset=features + [target])

df['Prod_Class'] = pd.qcut(
    df['Prod'],
    q=3,
    labels=['Low','Medium','Hight']
)

x = df[features]
y = df['Prod_Class']

x_train,x_test,y_train,y_test = tts(x,y,test_size=0.2,random_state=42)
model = LogisticRegression()
model.fit(x_train,y_train)

y_pred = model.predict(x_test)

def s(txt:str):
    a(txt,False)

s(f'Accuracy: {accuracy_score(y_test,y_pred):.2f}')