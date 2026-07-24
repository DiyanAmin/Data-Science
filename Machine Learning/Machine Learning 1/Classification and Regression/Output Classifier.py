from numpy import where
from collections import Counter
from sklearn.datasets import make_blobs
from matplotlib import pyplot as plt

x,y = make_blobs(n_samples=1000,centers=2,random_state=1)

print(f'[SHAPE] X shape: {x.shape}')
print(f'[SHAPE] Y shape: {y.shape}')

counter = Counter(y)
print(f'[*] Counter: {counter}')

for i in range(10):
    print(f'[DATA] {x[i]}')
    print(f'[DATA] {y[i]}')

for label,_ in counter.items():
    row_ix = where(y==label)[0]
    plt.scatter(x[row_ix,0],x[row_ix,1],label=str(label))
plt.legend()
plt.show()