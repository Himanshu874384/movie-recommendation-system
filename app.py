import streamlit as st
from recommender import recommend


st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="wide"
)

st.title("🎬 Movie Recommendation System")
st.write(
    "Get movie recommendations based on genre, director, and language."
)


movie_name = st.text_input(
    "Enter Movie Name",
    placeholder="Example: Movie_10"
)


num_recommendations = st.slider(
    "Number of Recommendations",
    min_value=1,
    max_value=10,
    value=5
)


if st.button("Recommend Movies"):

    if movie_name.strip() == "":
        st.warning("Please enter a movie name.")

    else:

        results = recommend(movie_name, num_recommendations)

        if len(results) > 0 and isinstance(results[0], str):
            st.error(results[0])

        else:

            st.success(
                f"Top {num_recommendations} recommendations for {movie_name}"
            )

            for movie in results:

                st.subheader(movie["title"])

                col1, col2 = st.columns(2)

                with col1:
                    st.write(f"**Genre:** {movie['genre']}")
                    st.write(f"**Director:** {movie['director']}")

                with col2:
                    st.write(f"**Language:** {movie['language']}")
                    st.write(f"**Rating:** ⭐ {movie['rating']}")

                st.write(
                    f"**Similarity Score:** {movie['similarity_score']}"
                )

                st.divider()