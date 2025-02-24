# Import the libraries
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re

# Load data
# Since the genres are grouped up in one collumn and seperated with '|', the genres need to be split
movies = pd.read_csv('movies.csv')
movies['processed_genres'] = movies['genres'].apply(lambda x: x.split('|'))
movies['genres_str'] = movies['processed_genres'].apply(lambda x: ' '.join(x))

# TF-IDF vectorization
vectorizer = TfidfVectorizer(stop_words='english')
tfidfMatrix = vectorizer.fit_transform(movies['genres_str'])

# Extract genres function
def extractGenres(userInput, allGenres):
    userInput = userInput.lower()
    extractedGenres = [genre for genre in allGenres if genre.lower() in userInput]
    return ' '.join(extractedGenres)

# Get similar movies function
def getSimilarMovies(userInput, tfidfMatrix, topN=5):
    userGenres = extractGenres(userInput, allGenres)
    if not userGenres:
        print("No relevant genres found in the user input.")
        return []
    userInput_tfidf = vectorizer.transform([userGenres])
    cosineSim = cosine_similarity(userInput_tfidf, tfidfMatrix)
    similarIndices = cosineSim[0].argsort()[-topN:][::-1]
    return [(movies.iloc[i]['movie_title'], cosineSim[0][i]) for i in similarIndices]

# Prepare all genres list
allGenres = sorted(set([genre for sublist in movies['processed_genres'] for genre in sublist]))

# Get user input
userInput = input("What movie genres do you feel like watching? ")
print("\nBased on your input, you may like the following top 5 picks. Enjoy! \n")

# Print the 5 suggested movies based on user input
similarMovies = getSimilarMovies(userInput, tfidfMatrix, topN=5)
if similarMovies:
    for title, score in similarMovies:
        print(f"{title} - Similarity Score: {score}")
print("\n")