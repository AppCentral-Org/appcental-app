from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_similarity(name1, name2):
    # Tokenization
    names = [name1, name2]
    
    # Initialize the TF-IDF vectorizer
    tfidf_vectorizer = TfidfVectorizer()
    
    # Fit the vectorizer to the names and transform the names into TF-IDF vectors
    tfidf_matrix = tfidf_vectorizer.fit_transform(names)
    
    # Calculate cosine similarity between the TF-IDF vectors
    similarity = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])[0][0]
    
    return similarity

# Example names
name1 = "John Doe"
name2 = "Jane Smith"

# Calculate similarity
similarity_score = calculate_similarity(name1, name2)
print("Similarity between '{}' and '{}': {:.2f}".format(name1, name2, similarity_score))
