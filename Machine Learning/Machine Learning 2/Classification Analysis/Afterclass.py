from pandas import read_csv as r

df = r('glass.csv')

for i in df.items():
    for j in i[1]: