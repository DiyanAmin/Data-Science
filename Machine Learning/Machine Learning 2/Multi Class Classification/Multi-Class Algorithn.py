from sklearn.linear_model import LogisticRegression
print('[IMPORT] Imported LogisticRegression from sklearn.linear_model')
from sklearn.datasets import load_iris
print('[IMPORT] Imported load_iris() from sklearn.datasets')
import numpy as np
print('[IMPORT] Imported numpy as np')
from matplotlib import pyplot as plt
print('[IMPORT] Imported pyplot as plt from matplotlib\n\n')

def s(txt:str):
    print(f'[OUTPUT] {txt}')

iris = load_iris()
x = iris.data[:,:2]
y = iris.target

model = LogisticRegression()
model.fit(x,y)

x_min,x_max = x[:,0].min() - 0.5, x[:,0].max() + 0.5
y_min,y_max = x[:,1].min() - 0.5, x[:,1].max() + 0.5

xx,yy = np.meshgrid(
    np.arange(x_min,x_max,0.02)
    ,
    np.arange(y_min,y_max,0.02)
)

z = model.predict(np.c_[xx.ravel(),yy.ravel()])
z = z.reshape(xx.shape)

plt.figure(
    1
    ,
    figsize=(4,3)
)

plt.pcolormesh(
    xx,
    yy,
    z,
    cmap=plt.cm.Paired
)

plt.scatter(x[:,0],x[:,1],c=y,edgecolors='k',cmap=plt.cm.Paired)
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')

plt.xlim(xx.min(),xx.max())
plt.ylim(yy.min(),yy.max())
plt.xticks(())
plt.yticks(())

plt.show()

s(f'Score: {model.score(x,y)}')
