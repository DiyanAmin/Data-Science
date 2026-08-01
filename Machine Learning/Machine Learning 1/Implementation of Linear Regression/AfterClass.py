def i(from_:bool=True,from__:str='',as_:str='',as__:bool=True,import_:str=''):
    statement:str = '[IMPORT] Imported '
    if from_:
        statement+=f'{import_} from {from__}'
        if as__:
            statement+=f' as {as_}'
    elif as__:
        statement+=f'{import_} as {as_}'
    print(statement)

import pandas as pd
i(from_=False,as__=True,as_='pd',import_='pandas')
import numpy as np
i(from_=False,as__=True,as_='np',import_='numpy')
from matplotlib import pyplot as plt
i(from__='matplotlib',import_='pyplot',as_='plt')

data = pd.read_csv('xydataset.csv',header=None)

data=data.drop(columns=[0])
data.columns=['x','y']

data = data.dropna()

print(f'[DATA] Null Values after cleaning:\n{data.isnull().any()}')

x = data['x'].values
y = data['y'].values

def gradient_descent():
    m = len(y)
    theta = np.zeros(2)

    cost