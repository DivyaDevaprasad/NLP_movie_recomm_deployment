import pandas as pd

data = pd.read_csv("movie_metadata.csv")
data.columns

#new_data = pd.DataFrame(data['actor_1_name','actor_2_name','actor_3_name','director_name','genres','movie_title'])

data.isnull().sum(axis =0)

import numpy as np

def impute_val(col,val):
    data[col] = data[col].replace(np.nan, val)
    
impute_val("actor_1_name","unknown")
impute_val("actor_2_name","unknown")
impute_val("actor_3_name","unknown")
impute_val("director_name","unknown")
    
data['genres'] = data['genres'].replace('|', ' ')

data['movie_title'] = data['movie_title'].str.lower()

data['movie_title'] = data['movie_title'].str[:-1]

data.to_csv('data.csv',index=False)