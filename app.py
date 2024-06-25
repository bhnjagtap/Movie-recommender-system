import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = request.get( 'http://www.omdbapi.com/?i=tt3896198&apikey=2dfa1f9'.format(movie_id))
    data = response.json()



def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]
    movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]


    recommended_movies = []
    recommended_movie_posters = []
    for i in movie_list:
        movie_id = i[0]
        #fetch poster
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movie_posters.append(fetch_poster(movie_id))
    return recommended_movies





movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    "How would you like to be contacted?",
    movies['title'].values)

#st.button("recommend", type="primary")
if st.button("recommend"):
    names, posters = recommend(selected_movie_name)
    for i in recomendations:
        st.write(i)


