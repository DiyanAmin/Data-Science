def a(txt:str):
    print(f'[OUTPUT] {txt}')

def s(msg:str):
    print(f'[IMPORT] {msg}')

import pandas as pd
s('Imported pandas as pd')
import numpy as np
s('Imported numpy as np')
from sklearn.model_selection import train_test_split as tts
s('Imported train_test_split() as tts() fom sklearn.model_selection')
from sklearn.datasets import make_classification as mc
s('Imported make_classification() as mc() from sklearn.datasets')
from sklearn.linear_model import LogisticRegression
s('Imported LogisticRegression from sklearn.linear_model')
from sklearn.metrics import accuracy_score,classification_report
s('Imported accuracy_score() and classification_report() from sklearn.metrics')
from matplotlib import pyplot as plt
s('Imported pyplot as plt from matplotlib\n\n')

plt.rcParams.update({
    
})