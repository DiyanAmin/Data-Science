from funcs import import_ as s
s('Imported import_() as s from funcs.py')

import numpy as np
s('Imported numpy as np')

from sklearn.linear_model import LogisticRegression
s('Imported LogisticRegression from sklearn.linear_model')

from sklearn.metrics import classification_report, confusion_matrix
s('Imported classification_report() and confusion_matrix() from sklearn.metrics')

from funcs import output as a
s('Imported output() as a from funcs.py')

x = np.arange(10).reshape(-1,1)
y = np.array([0,1,0,0,1,1,1,1,1,1])

model = LogisticRegression(solver='liblinear',C=10.0,random_state=0)
model.fit(x,y)

p_pred = model.predict_proba(x)
y_pred = model.predict(x)
score_ = model.score(x,y)
conf_m = confusion_matrix(y,y_pred)
report = classification_report(y,y_pred)

a(f'x:\n{x}')
a(f'y:\n{y}\n\n')

a(f'Intercept:{model.intercept_}')
a(f'Co-efficient: {model.coef_}\n\n')

a(f'p_pred:\n{p_pred}\n\n')
a(f'y_pred:{y_pred}\n\n')

