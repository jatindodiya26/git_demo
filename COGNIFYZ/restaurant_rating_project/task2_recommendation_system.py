import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# load dataset
data = pd.read_csv("C:\\Users\\Lenovo\\OneDrive\\Desktop\\COGNIFYZ\\restaurant_rating_project\\restaurant_data.csv")

# remove missing values
data = data.dropna()

print(data.head())

# Create combined feature
data['features'] = data['Cuisines'] + " " + data['Average Cost for two'].astype(str)

# Convert text to numerical data
vectorizer = CountVectorizer()
feature_matrix = vectorizer.fit_transform(data['features'])

# Compute similarity
similarity = cosine_similarity(feature_matrix)

# Function to recommend restaurants
def recommend_restaurant(name):

    restaurant_index = data[data['Restaurant Name'] == name].index[0]

    similar_restaurants = list(enumerate(similarity[restaurant_index]))

    sorted_restaurants = sorted(similar_restaurants, key=lambda x: x[1], reverse=True)

    recommended = data.iloc[[i[0] for i in sorted_restaurants[1:6]]]

    recommended = recommended.sort_values(by="Aggregate rating", ascending=False)

    print("\nRecommended Restaurants:\n")
    print(recommended[['Restaurant Name','Aggregate rating']])

# Call the function
recommend_restaurant("Dominos Pizza")