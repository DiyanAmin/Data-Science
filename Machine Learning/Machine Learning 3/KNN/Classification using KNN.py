import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sb
from sklearn.model_selection  import train_test_split as tts
from sklearn.neighbors import KNeighborsClassifier

data = pd.read_csv('sample_data.csv',sep=',')
print(data.head())

y = data.pop('TARGET CLASS')
x = data
x_train,x_test,y_train,y_test = tts(x,y,test_size=0.2)

error_rates = []

predictions = []
for a in range(1,40):
    knn = KNeighborsClassifier(n_neighbors=a)
    knn.fit(x_train,y_train)
    preds = knn.predict(x_test)
    error_rates.append(np.mean(y_test-preds))
    predictions.append(preds)

additional_data = {
    'Predictions':predictions,
    'Error Rates':error_rates

}

print(f'\n\n\n\n\nAdditional Data:\n{additional_data}\n\n\n\n')

plt.figure(figsize=(10,7))
plt.plot(range(1,40),error_rates,color='blue',linestyle='dotted',marker='o',markerfacecolor='red',markersize=10)

plt.title('Error Rate VS K value')
plt.xlabel('K values')
plt.ylabel('Error rates')
plt.show()  