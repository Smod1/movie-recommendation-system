# movie-recommendation-system
A content-based movie recommendation system built with Python and Flask. The application recommends movies similar to a selected title by analyzing movie metadata such as genres, keywords, cast, crew, overview, and tagline.

The recommendation engine uses TF-IDF vectorization and cosine similarity to measure how similar movies are to one another.

The recommendation pipeline consists of several stages:

TMDB Movie Data
      │
      ▼
Data Cleaning & Merging
      │
      ▼
Feature Engineering
      │
      ▼
Text Preprocessing
      │
      ▼
TF-IDF Vectorization
      │
      ▼
Cosine Similarity
      │
      ▼
Precomputed Similarity Matrix
      │
      ▼
Flask Web Application
      │
      ▼
Movie Recommendations

Flask was used here as a web application framework. This was my first time using flask, so the interface is not detailed.
