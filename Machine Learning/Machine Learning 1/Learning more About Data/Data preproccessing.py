import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

titanic = pd.read_csv(r'Titanic Dataset.csv')
titanic.head()

titanic.shape
titanic.isnull().sum()

sb.heatmap(titanic.isnull(),cmap='spring')

titanic.head()



titanic.dropna(inplace=True)

sb.heatmap(titanic.isnull(),cbar=False)

titanic.isnull().sum()

pd.get_dummies(titanic['Gender']).head()

gender = pd.get_dummies(titanic['Gender'],drop_first=True)

gender.head(4)
pd.get_dummies(titanic['Embarked']).head()

embarked = pd.get_dummies(titanic['Embarked'],drop_first=True)

pclass = pd.get_dummies(titanic['Pclass'],drop_first=True)

pclass.head(4)

titanic = pd.concat([titanic,gender,pclass],axis=1)
titanic.head()