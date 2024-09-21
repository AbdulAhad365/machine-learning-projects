import streamlit as st
import pickle
import pandas as pd
import requests

movies_dict=pickle.load(open("movies_dict.pkl","rb"))
movies=pd.DataFrame(movies_dict)
similarity=pickle.load(open("similarity.pkl","rb"))
movies_list=movies_dict["title"].values()

def fetch_api(movie_id):
    store=f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=5713dd77cb298449e3b714c1d8171756&append_to_response=videos'
    store=requests.get(store)
    in_json=store.json()
    return in_json
    # return "https://image.tmdb.org/t/p/w185/"+in_json["poster_path"]

def recommend(movie):
    movie_index = int(movies[movies['title']==movie].index[0])  # Get the index of the movie (make sure this is done correctly)
    distance = similarity[movie_index]
    movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]
    movie_names=[]
    movie_poster=[]
    for i in movie_list:  # Change movie_index to movie_list
        movie_names.append((movies.iloc[i[0]].title))
        #movie id
        movie_id=movies.iloc[i[0]].movie_id
        sti=fetch_api(movie_id)
        poster_path=sti.get("poster_path")
        movie_poster.append(poster_path)
    return movie_names,movie_poster

# print(movies_list)
#now extract values
# print(r)


st.title("Movies Recommendation System")
option=st.selectbox('Select the movies',movies_list)

#now the button to recommend
if st.button('Recommend'):
    names,poster=recommend(option)
    # for i in store:
    #     st.write(i) 
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.header(names[0])
        st.image(f"https://image.tmdb.org/t/p/w500{poster[0]}")
    with col2:
        st.header(names[1])
        st.image(f"https://image.tmdb.org/t/p/w500{poster[1]}")


    with col3:
        st.header(names[2])
        st.image(f"https://image.tmdb.org/t/p/w500{poster[2]}")

    with col4:
        st.header(names[3])
        st.image(f"https://image.tmdb.org/t/p/w500{poster[3]}")

    with col5:
        st.header(names[4])
        st.image(f"https://image.tmdb.org/t/p/w500{poster[4]}")