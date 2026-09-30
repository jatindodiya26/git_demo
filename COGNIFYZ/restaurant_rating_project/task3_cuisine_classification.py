import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# load dataset

data = pd.read_csv("C:\\Users\\Lenovo\\OneDrive\\Desktop\\COGNIFYZ\\restaurant_rating_project\\restaurant_data.csv")


print(data.info())
print(data.head())
data.dropna(inplace=True)
# We will predict Cuisine using restaurant name + cost.
data['features'] = data['Restaurant Name'] + " " + data['Average Cost for two'].astype(str)

X = data['features']
y = data['Cuisines']

# Convert text features into a matrix of token counts
vectorizer = CountVectorizer()

X_vector = vectorizer.fit_transform(X)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X_vector, y, test_size=0.2, random_state=42
)

# Train a Random Forest Classifier

model = RandomForestClassifier()

model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, predictions)

print("Model Accuracy:", accuracy)

print("\nClassification Report:\n")
print(classification_report(y_test, predictions))

# Example usage
sample = vectorizer.transform(["Dominos 500"])

prediction = model.predict(sample)

print("\nPredicted Cuisine:", prediction[0])