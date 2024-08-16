import pandas as pd

# Load the data
print("Loading data...")
ratings_df = pd.read_csv('ratings.csv', nrows=5000000)
movies_df = pd.read_csv('movies.csv')

# Extract the release year from the title
movies_df['year'] = movies_df['title'].str.extract(r'\((\d{4})\)').astype(float)

# Comprehensive Recommendations (All Movies)
def recommend_movies(selected_genre, recent=False):
    if recent:
        filtered_movies_df = movies_df[movies_df['year'] >= 2014]
    else:
        filtered_movies_df = movies_df

    # Merge the datasets
    merged_df = pd.merge(ratings_df, filtered_movies_df, on='movieId')

    # Filter movies by genre
    genre_movies = merged_df[merged_df['genres'].str.contains(selected_genre, case=False)]

    # Calculate the number of ratings per movie in the selected genre
    genre_rating_counts = genre_movies.groupby('title')['rating'].count()

    # Calculate the average rating for each movie in the selected genre
    average_ratings_genre = genre_movies.groupby('title')['rating'].mean()

    # Define a threshold for the minimum number of ratings
    min_ratings_genre = 100  # Adjust this value as needed

    # Filter movies that have more than the minimum number of ratings in the genre
    popular_genre_movies = average_ratings_genre[genre_rating_counts > min_ratings_genre]

    # Sort movies by their average rating (descending)
    sorted_genre_movies = popular_genre_movies.sort_values(ascending=False)

    # Display the top 10 movies in the selected genre
    print(f"\nTop 10 {selected_genre} Movies (with at least {min_ratings_genre} ratings):")
    print(sorted_genre_movies.head(10))

# Example Usage
print("\n--- Comprehensive Recommendations ---")
recommend_movies(selected_genre='Horror', recent=False)

print("\n--- Recent Movies Recommendations ---")
recommend_movies(selected_genre='Horror', recent=True)
[ec2-user@ip-172-31-84-123 ~]$  cat app.py
from flask import Flask, jsonify, request, render_template
import pandas as pd

app = Flask(__name__)

# Load the data
print("Loading data...")
ratings_df = pd.read_csv('ratings.csv', nrows=2000000)
movies_df = pd.read_csv('movies.csv')

# Extract the release year from the title
movies_df['year'] = movies_df['title'].str.extract(r'\((\d{4})\)').astype(float)

def get_recommendations(selected_genre, recent=False):
    print(f"Selected genre: {selected_genre}, Recent: {recent}")

    # Filter by recency if needed
    if recent:
        filtered_movies_df = movies_df[movies_df['year'] >= 2014]
    else:
        filtered_movies_df = movies_df

    if selected_genre == "All Genres":
        # Consider all movies, without filtering by genre
        genre_movies = pd.merge(ratings_df, filtered_movies_df, on='movieId')
    else:
        # Filter movies by genre
        genre_movies = pd.merge(ratings_df, filtered_movies_df, on='movieId')
        genre_movies = genre_movies[genre_movies['genres'].str.contains(selected_genre, case=False, na=False)]

    # Check if DataFrame is empty or if 'title' column exists
    if genre_movies.empty or 'title' not in genre_movies.columns:
        print("No movies found for the selected criteria.")
        return {}  # Return an empty dictionary if no movies match the criteria

    # Calculate the number of ratings per movie
    genre_rating_counts = genre_movies.groupby('title')['rating'].count()

    # Calculate the average rating for each movie
    average_ratings_genre = genre_movies.groupby('title')['rating'].mean()

    # Define a threshold for the minimum number of ratings
    min_ratings_genre = 100  # Adjust this value as needed

    # Filter movies that have more than the minimum number of ratings
    popular_genre_movies = average_ratings_genre[genre_rating_counts > min_ratings_genre]

    # Sort movies by their average rating (descending)
    sorted_genre_movies = popular_genre_movies.sort_values(ascending=False)

    # Return the top 10 movies
    return sorted_genre_movies.head(10).round(2).to_dict()

@app.route('/')
def index():
    genres = ['Action', 'Comedy', 'Drama', 'Thriller', 'Adventure', 'Romance', 'Crime', 'Science Fiction', 'Fantasy', 'Horror', 'Documentary', 'All Genres']
    return render_template('index.html', genres=genres)

@app.route('/recommend', methods=['GET', 'POST'])
def recommend():
    if request.method == 'POST':
        genre = request.form.get('genre', default='Action')
        recency = request.form.get('recency', default='all')
        recent = recency == 'recent'
    else:
        genre = request.args.get('genre', default='Action', type=str)
        recent = request.args.get('recent', default=False, type=bool)

    recommendations = get_recommendations(genre, recent)
    return render_template('results.html', recommendations=recommendations, genre=genre, recent=recent)

@app.route('/movie-picker')
def movie_picker():
    genres = ['Action', 'Comedy', 'Drama', 'Thriller', 'Adventure', 'Romance', 'Crime', 'Sci-Fi', 'Fantasy', 'Horror', 'Documentary', 'All Genres']
    return render_template('index.html', genres=genres)

@app.route('/genres')
def genres():
    genres = ['Action', 'Comedy', 'Drama', 'Thriller', 'Adventure', 'Romance', 'Crime', 'Sci-Fi', 'Fantasy', 'Horror', 'Documentary', 'All Genres']
    return render_template('index.html', genres=genres)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
[ec2-user@ip-172-31-84-123 ~]$ cat movie_analysis.py
import pandas as pd

# Load the data
print("Loading data...")
ratings_df = pd.read_csv('ratings.csv', nrows=5000000)
movies_df = pd.read_csv('movies.csv')

# Extract the release year from the title
movies_df['year'] = movies_df['title'].str.extract(r'\((\d{4})\)').astype(float)

# Comprehensive Recommendations (All Movies)
def recommend_movies(selected_genre, recent=False):
    if recent:
        filtered_movies_df = movies_df[movies_df['year'] >= 2014]
    else:
        filtered_movies_df = movies_df

    # Merge the datasets
    merged_df = pd.merge(ratings_df, filtered_movies_df, on='movieId')

    # Filter movies by genre
    genre_movies = merged_df[merged_df['genres'].str.contains(selected_genre, case=False)]

    # Calculate the number of ratings per movie in the selected genre
    genre_rating_counts = genre_movies.groupby('title')['rating'].count()

    # Calculate the average rating for each movie in the selected genre
    average_ratings_genre = genre_movies.groupby('title')['rating'].mean()

    # Define a threshold for the minimum number of ratings
    min_ratings_genre = 100  # Adjust this value as needed

    # Filter movies that have more than the minimum number of ratings in the genre
    popular_genre_movies = average_ratings_genre[genre_rating_counts > min_ratings_genre]

    # Sort movies by their average rating (descending)
    sorted_genre_movies = popular_genre_movies.sort_values(ascending=False)

    # Display the top 10 movies in the selected genre
    print(f"\nTop 10 {selected_genre} Movies (with at least {min_ratings_genre} ratings):")
    print(sorted_genre_movies.head(10))

# Example Usage
print("\n--- Comprehensive Recommendations ---")
recommend_movies(selected_genre='Horror', recent=False)

print("\n--- Recent Movies Recommendations ---")