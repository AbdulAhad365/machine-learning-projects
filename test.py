import streamlit as st
import requests

# Replace with your own API key
api_key = "your_api_key"
movie_id = 157336  # Example movie ID for "Interstellar"

# Fetch movie details
def store(movie):
        url = f"https://api.themoviedb.org/3/movie/{movie}?api_key=5713dd77cb298449e3b714c1d8171756"
        response = requests.get(url)
        data = response.json()
        return data

# Extract poster path and construct full URL
sti=store(157336)
poster_path = sti.get("poster_path")
if poster_path:
    poster_url = f"https://image.tmdb.org/t/p/w500{poster_path}"
    st.image(poster_url)
else:
    st.write("Poster not found")
