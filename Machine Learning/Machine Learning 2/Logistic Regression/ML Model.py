from funcs import import_ as s
s('Imported import_() as s from funcs.py')

from funcs import output as a
s('Imported output() as s from funcs.py')

import numpy as np
s('Imported numpy as np')

from sklearn.linear_model import LogisticRegression
s('Imported LogisticRegression from sklearn.linear_model')

from sklearn.model_selection import train_test_split
s('Imported train_test_split() from sklearn.model_selection')

from sklearn.metrics import classification_report
s('Imported classification_report() from sklearn.metrics')



x = np.arange(10).reshape(-1, 1)
y = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1, 1])

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.03,random_state=12)

model = LogisticRegression()
model.fit(x_train,y_train)

y_pred = model.predict(x_test)
a(f'Classification Report:\n{classification_report(y_test,y_pred)}')

n_classes = len(np.unique)
    a('This')