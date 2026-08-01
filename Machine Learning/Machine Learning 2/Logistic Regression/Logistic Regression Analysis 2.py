from funcs import import_ as s
s('Imported import_() as s from funcs.py')

from funcs import output as a
s('Imported output() as a from funcs.py')

from sklearn.datasets import make_classification as mc
s('Imported make_classification() as mc from sklearn.datasets')

from matplotlib import pyplot as plt
s('Imported pyplot as plt from matplotlib')

from sklearn.linear_model import LogisticRegression
s('Imported LogisticRegression from sklearn.linear_model')

from sklearn.model_selection import train_test_split
s('Imported train_test_split() from sklearn.model_selection')

from sklearn.metrics import confusion_matrix
s('Imported confusion_matrix() from sklearn.metrics')

import pandas as pd
s("Imported pandas as pd")

x,y = mc(
    n_samples=100,
    n_features=1,
    n_classes=2,
    n_clusters_per_class=1,
    flip_y=0.03,
    n_informative=1,
    n_redundant=0,
    n_repeated=0
)

plt.scatter(x,y,c=y,cmap='rainbow')
plt.title('Scatter Plot of Logistic Regression')
plt.show()

x_train,x_test,y_train,y_test = train_test_split(x,y,random_state=1)

log_reg = LogisticRegression()
log_reg.fit(x_train,y_train)

a(f'\n\nCo-efficient: {log_reg.coef_}')
a(f'Intercept: {log_reg.intercept_}')

y_pred = log_reg.predict(x_test)

a(f'y_pred: {y_pred}')