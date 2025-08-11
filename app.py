import pickle
import streamlit as st
import numpy as np

st.header('Book Recommender System Using Machine Learning')

# Load your artifacts
model = pickle.load(open('artifacts/model.pkl', 'rb'))
book_names = pickle.load(open('artifacts/book_names.pkl', 'rb'))
final_rating = pickle.load(open('artifacts/final_rating.pkl', 'rb'))
book_pivot = pickle.load(open('artifacts/book_pivot.pkl', 'rb'))

def fetch_poster(suggestions):
    poster_urls = []
    for book_id in suggestions[0]:
        book_name = book_pivot.index[book_id]
        book_info = final_rating[final_rating['title'] == book_name]
        if not book_info.empty:
            url = book_info.iloc[0]['image_url']
            if url and isinstance(url, str) and url.strip() != "":
                poster_urls.append(url)
            else:
                poster_urls.append("https://via.placeholder.com/150?text=No+Image")
        else:
            poster_urls.append("https://via.placeholder.com/150?text=No+Image")
    return poster_urls

def recommend_book(book_name):
    try:
        book_id = np.where(book_pivot.index == book_name)[0][0]
    except IndexError:
        st.error("Book not found!")
        return [], []

    distances, suggestions = model.kneighbors(
        book_pivot.iloc[book_id, :].values.reshape(1, -1), n_neighbors=6
    )

    recommended_books = []
    for i in suggestions[0]:
        recommended_books.append(book_pivot.index[i])

    poster_urls = fetch_poster(suggestions)
    return recommended_books, poster_urls

selected_book = st.selectbox("Type or select a book from the dropdown", book_names)

if st.button('Show Recommendation'):
    recommended_books, poster_urls = recommend_book(selected_book)

    if recommended_books:
        st.subheader("Recommended Books:")
        cols = st.columns(4)

        # Skip the first book because it is the same book
        for idx, col in enumerate(cols):
            if idx+1 < len(recommended_books):
                col.text(recommended_books[idx+1])
                col.image(poster_urls[idx+1])
    else:
        st.write("No recommendations found.")

