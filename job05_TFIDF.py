import pickle

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.io import mmwrite, mmread

df_reviews = pd.read_csv('./cleaned_data/cleaned_reviews.csv')
df_reviews.dropna(inplace=True)
# df_reviews.to_csv('./cleaned_data/cleaned_reviews.csv',index=False)
df_reviews.info()

tfidf = TfidfVectorizer(sublinear_tf=True)
tfidf_matrix = tfidf.fit_transform(df_reviews['reviews'])
print(tfidf_matrix.shape)
print(tfidf_matrix[0])

with open('./models/tfidf.pickle', 'wb') as f:
    pickle.dump(tfidf, f)

mmwrite('./models/tfidf_movie_reviews.mtx', tfidf_matrix)
