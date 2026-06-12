import pandas as pd
import random

genres = [
    "Action", "Comedy", "Drama", "Sci-Fi",
    "Thriller", "Romance", "Adventure", "Fantasy"
]

directors = [
    "Raj Mehta", "Ankit Sharma", "Priya Singh",
    "Rahul Verma", "Neha Kapoor", "Arjun Gupta"
]

languages = [
    "English", "Hindi", "Spanish", "French"
]

data = []

for i in range(1, 1001):
    movie = {
        "movie_id": i,
        "title": f"Movie_{i}",
        "genre": ", ".join(random.sample(genres, random.randint(1, 3))),
        "director": random.choice(directors),
        "language": random.choice(languages),
        "release_year": random.randint(2000, 2025),
        "rating": round(random.uniform(1.0, 10.0), 1),
        "duration_min": random.randint(80, 180),
        "popularity": random.randint(1, 10000)
    }

    data.append(movie)

df = pd.DataFrame(data)

df.to_csv("synthetic_movies_dataset.csv", index=False)

print("Dataset Generated Successfully!")
print(df.head())