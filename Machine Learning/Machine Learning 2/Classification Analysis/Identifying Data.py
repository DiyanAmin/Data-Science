import numpy as np
print('[IMPORT] Imported numpy as np')
import seaborn as sb
print('[IMPORT] Imported seaborn as sb')
from matplotlib import pyplot as plt
print('[IMPORT] Imported pyplot as plt from matplotlib')
from sklearn.datasets import load_breast_cancer
print('[IMPORT] Imported load_breast_cancer from sklearn.datasets')

dataset = load_breast_cancer()

sb.set_style('dark')
plt.style.use(['https://gist.githubusercontent.com/BrendanMartin/01e71bb9550774e2ccff3af7574c0020/raw/6fa9681c7d0232d34c9271de9be150e584e606fe/lds_default.mplstyle'])

plt.rcParams.update({'figure.figsize':(8,6),'axes.titlepad':22.0})

print(f'[OUTPUT] Target variables: {dataset['target_names']}')
(unique,counts) = np.unique(dataset['target'],return_counts=True)

print(f'[OUTPUT] Unique Values of Target Variable: {unique}')
print(f'[OUTPUT] Counts of target variable: {counts}')

sb.barplot(x=dataset['target_names'],y=counts)
plt.title('Target Variable Counts in dataset')
plt.show()