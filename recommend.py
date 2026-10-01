#This Python code is used to run the model by giving movie title as input and get top 5 similar movies as output
# Note : before runnning the below snippet just make sure you downloaded the DF.pkl and vectors.pkl

import joblib
from sklearn.metrics.pairwise import cosine_similarity

DF = joblib.load('DF.pkl')
vectors = joblib.load('vectors.pkl')

similarity = cosine_similarity(vectors)

def recommend(movie):
    movie_index = DF[DF['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

    for i in movie_list:
        print(DF.iloc[i[0]].title)

recommend('Aliens vs Predator: Requiem')

# Try with these movies :
# Aliens vs Predator: Requiem
# Battle: Los Angeles
# Predator
# Independence Day
# Falcon Rising