import pandas as pd
print('[IMPORT] Imported pandas as pd')
from numpy import sqrt
print("[IMPORT] Imported sqrt from numpy")
from sklearn.model_selection import train_test_split
print('[IMPORT] Imported train_test_split from sklearn.model_selection')
from sklearn.linear_model import LinearRegression
print('[IMPORT] Imported LinearRegression from sklearn.linear_model')
from sklearn.metrics import mean_squared_error, mean_absolute_error
print('[IMPORT] Imported mean_squared_error and mean_absolute_error from sklearn.metrics\n')

dataset = pd.read_csv('petrol_consumption.csv')

print(dataset.head())

x = dataset[['Petrol_tax','Average_income','Paved_Highways','Population_Driver_licence(%)']]
y = dataset['Petrol_Consumption']

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=0)

regressor = LinearRegression()
regressor.fit(x_train,y_train)

coeff_df = pd.DataFrame(regressor.coef_,x.columns,columns=['Coefficient'])
print(f'[DATAFRAME] coeff_df:\n\n{coeff_df}\n\n')

y_pred = regressor.predict(x_test)
df = pd.DataFrame(
    {
        'Actual':y_test,
        'Predicted':y_pred
    }
)
print(f'[DATAFRAME] df:\n\n{df}\n\n')


#Metrics
print(f'[METRICS] Means Absolute Error: {mean_absolute_error(y_test,y_pred)}')
print(f'[METRICS] Means Squared Error: {mean_squared_error(y_test,y_pred)}')
print(f'[METRICS] Root Mean Absolute Error: {sqrt(mean_squared_error(y_test,y_pred))}')