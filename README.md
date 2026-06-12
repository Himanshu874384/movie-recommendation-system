# 🎬 Movie Recommendation System

A content-based Movie Recommendation System built using Python, Pandas, Scikit-Learn, and Streamlit.

## Features

- Recommend similar movies based on:
  - Genre
  - Director
  - Language
- Interactive Streamlit web interface
- Synthetic movie dataset generated from scratch
- Cosine Similarity based recommendations
- Adjustable number of recommendations

## Tech Stack

- Python
- Pandas
- Scikit-Learn
- Streamlit

## Project Structure

```
movie-recommendation-system/
│
├── app.py
├── recommender.py
├── synthetic_movies_dataset.csv
└── README.md
```

## How It Works

1. Movie metadata is combined into a single feature column.
2. TF-IDF Vectorization converts text into numerical vectors.
3. Cosine Similarity calculates similarity between movies.
4. The system recommends the most similar movies.

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/movie-recommendation-system.git
```

Install dependencies:

```bash
pip install pandas scikit-learn streamlit
```

Run the application:

```bash
streamlit run app.py
```

## Sample Recommendation

Input:

```
Movie_10
```

Output:

```
Movie_959
Movie_274
Movie_635
Movie_121
Movie_448
```

## Future Improvements

- Movie posters
- User authentication
- Hybrid recommendation system
- Collaborative filtering
- Real movie dataset integration

## Author

Himanshu Mishra
