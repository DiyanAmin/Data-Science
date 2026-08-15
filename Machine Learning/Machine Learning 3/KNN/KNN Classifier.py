from pandas import read_csv as r
from matplotlib import pyplot as plt
import numpy as np

from sklearn.model_selection import train_test_split as tts
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report,accuracy_score,confusion_matrix

df = r('Iris Dataset.csv',sep=',')
print(df.head())

print(df.isnull().sum())

le = LabelEncoder()
df['Species'] = le.fit_transform(df['Species'])

x = df.drop('Species',axis=1)
y = df['Species']

x_train,x_test,y_train,y_test = tts(x,y,test_size=0.2,random_state=42)

model = LogisticRegression()
model.fit(x_train,y_train)
y_pred = model.predict(x_test)

error_rates = []

for k in range(1,40):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(x_train,y_train)
    pred = knn.predict(x_test)
    error  = np.mean(pred!=y_test)
    error_rates.append(error)

#Best K
best_k = error_rates.index(min(error_rates)) + 1
print(f'\n\n\n\n\nBest k found: {best_k}')

knn = KNeighborsClassifier()
knn.fit(x_train,y_train)
y_pred = knn.predict(x_test)

acc = accuracy_score(y_test,y_pred)
print(f'\nAccuracy: {acc:.2f}')
print(f'\nClassification Report:\n{classification_report(y_test,y_pred,target_names=le.classes_)}')
print(f'\nConfusion Matrix:\n{confusion_matrix(y_test,y_pred)}\n\n\n\n\n')
#----------

#Plot
plt.figure(figsize=(10,6))
plt.plot(range(1,40),error_rates,color='blue',linestyle='dotted',marker='o',markerfacecolor='red',markersize=10)

plt.title('Error rates VS K values')
plt.xlabel('K values')
plt.ylabel('Error rates')

plt.show()

