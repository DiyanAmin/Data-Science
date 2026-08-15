import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

def diyan_sqrt(x):
    return x**0.5 # x^(1/2)

rdf  = pd.read_csv('ratings.csv')
print(rdf.head())

mdf = pd.read_csv('movies.csv', sep=',', quotechar='"', engine='python',on_bad_lines='skip')
print(mdf.head())

mdf['year'] = mdf['title'].str.extract(r'(\(\d\d\d\d\))',expand=True)
print(mdf.head())

mdf['year'] = mdf['year'].str.extract(r'(\d\d\d\d)',expand=True)
print(mdf.head())

mdf['title'] = mdf['title'].str.replace(r'(\(\d\d\d\d\))','')
print(mdf.head())

mdf['title'] = mdf['title'].apply(lambda x:x.strip())

mdf['genres'] = mdf['genres'].str.split('|')
print(mdf.head())


m_copy = mdf.copy()

for index,row in mdf.iterrows():
    for genre in row['genres']:
        m_copy.at[index,genre] = 1

print(m_copy.head())

m_copy = m_copy.fillna(0)

print(m_copy.head())

print(rdf.head())

rdf = rdf.drop(
    ['timestamp'],
    axis=1
)

print(rdf.head())

print('Please give some user input.\n\n')

user_input = []


movies_num = int(input('How many movies did you watch?\n>'))

while len(user_input)!=movies_num:
    movie_details = {}
    title = input('\nEnter movie title\n>')
    movie_details['title'] = title
    ratings = float(input('Enter movie rating\n>'))
    movie_details['rating'] = ratings
    user_input.append(movie_details)
    movie_details = {}

minp = pd.DataFrame(user_input)
print(minp)

inp_id = mdf[mdf['title'].isin(minp['title'].tolist())]

minp = pd.merge(inp_id,minp)
print(minp)

minp = minp.drop(['genres','year'],axis=1)
print(minp)

m_user = m_copy[m_copy['movieId'].isin(minp['movieId'].tolist())]
print(m_user)

ugt = m_user.drop(
    [
        'movieId',
        'title',
        'genres',
        'year'
    ],
    axis=1
)

print(ugt)

up = ugt.transpose().dot(minp['rating'])
print(up)

gt = m_copy.set_index(m_copy['movieId'])
print(gt)

gt = gt.drop(
    [
        'movieId',
        'title',
        'genres',
        'year'
    ],
    axis=1
)
print(gt.head())

recdf = ((gt*up).sum(axis=1))/up.sum()
recdf = pd.DataFrame(recdf)
print(recdf.head())

recdf = recdf.sort_values(ascending=False)
recdf = pd.DataFrame(recdf)
print(recdf.head())

rt = mdf.loc[mdf['movieId'].isin(rdf.head(20).keys())]
print(rt)