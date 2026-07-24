from matplotlib import pyplot as plt
import numpy as np
from sklearn import  datasets,linear_model
from sklearn.metrics import mean_squared_error,r2_score

diabetesX,diabetesY = datasets.load_diabetes(return_X_y=True)

diabetesX = diabetesX[:,np.newaxis,2]

diabetesX_train = diabetesX[:-20]
diabetesX_test = diabetesX[-20:]

diabetesY_train = diabetesY[:-20]
diabetesY_test = diabetesY[-20:]

regr = linear_model.LinearRegression()

regr.fit(diabetesX_train,diabetesY_train)

diabetesY_pred = regr.predict(diabetesX_test)

print(f'Coefficients:\n{regr.coef_}')
print('Mean squared error: %.2f'% mean_squared_error(diabetesY_test,diabetesY_pred))
print('Coefficient of determination: %.2f'% r2_score(diabetesY_test,diabetesY_pred))

plt.scatter(diabetesX_test,diabetesY_test,color='black')
plt.plot(diabetesX_test,diabetesY_pred,color='blue',linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()