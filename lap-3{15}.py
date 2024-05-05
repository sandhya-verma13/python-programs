# Dictionary representing user preferences for movies
user_preferences = {
    "action": ["The Dark Knight", "Inception", "Mad Max: Fury Road"],
    "comedy": ["Superbad", "The Hangover", "Anchorman"],
    "drama": ["The Shawshank Redemption", "Forrest Gump", "The Godfather"],
    "sci-fi": ["Interstellar", "Blade Runner 2049", "The Matrix"]
}

# Function to recommend movies based on user preferences
def recommend_movies(preferences):
    recommended_movies = []

    for genre, movies in preferences.items():
        recommended_movies.extend(movies)

    return recommended_movies

# Get user preferences
print("Enter your preferred movie genres (comma-separated): ")
genres_input = input().strip().split(',')
user_genres = [genre.strip() for genre in genres_input]

# Filter movies based on user preferences
user_movies = recommend_movies({genre: user_preferences[genre] for genre in user_genres})

# Print recommended movies
print("Recommended Movies:")
for movie in user_movies:
    print(movie)

