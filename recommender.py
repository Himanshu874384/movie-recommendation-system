import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
df = pd.read_csv("synthetic_movies_dataset.csv")

# Fill missing values (if any)
df.fillna("", inplace=True)

# Combine features
df["features"] = (
    df["genre"] + " " +
    df["director"] + " " +
    df["language"]
)

# Convert text features into numerical vectors
vectorizer = TfidfVectorizer()
feature_vectors = vectorizer.fit_transform(df["features"])

# Compute similarity matrix
similarity_matrix = cosine_similarity(feature_vectors)


def recommend(movie_title, top_n=5):
    """
    Recommend similar movies based on genre, director, and language.
    """

    # Check if movie exists
    if movie_title not in df["title"].values:
        return ["Movie not found!"]

    # Get movie index
    movie_index = df[df["title"] == movie_title].index[0]

    # Get similarity scores
    similarity_scores = list(
        enumerate(similarity_matrix[movie_index])
    )

    # Sort by similarity score
    similarity_scores = sorted(
        similarity_scores,
        key=lambda x: x[1],
        reverse=True
    )

    recommendations = []

    # Skip first movie (itself)
    for idx, score in similarity_scores[1:top_n + 1]:
        recommendations.append({
            "title": df.iloc[idx]["title"],
            "genre": df.iloc[idx]["genre"],
            "director": df.iloc[idx]["director"],
            "language": df.iloc[idx]["language"],
            "rating": df.iloc[idx]["rating"],
            "similarity_score": round(score, 3)
        })

    return recommendations


# Example usage
if __name__ == "__main__":
    movie_name = input("Enter movie name: ")

    results = recommend(movie_name)

    print("\nRecommended Movies:\n")

    for movie in results:
        if isinstance(movie, str):
            print(movie)
        else:
            print(f"Title: {movie['title']}")
            print(f"Genre: {movie['genre']}")
            print(f"Director: {movie['director']}")
            print(f"Language: {movie['language']}")
            print(f"Rating: {movie['rating']}")
            print(f"Similarity Score: {movie['similarity_score']}")
            print("-" * 40)