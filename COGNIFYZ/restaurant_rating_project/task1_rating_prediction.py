import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# load dataset
data = pd.read_csv("C:\\Users\\Lenovo\\OneDrive\\Desktop\\COGNIFYZ\\restaurant_rating_project\\restaurant_data.csv")


print(data.info())

# remove missing values
data = data.dropna()

print("Dataset after removing missing values:", data.shape)

X = data[['Votes', 'Average Cost for two']]
y = data['Aggregate rating']

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

from sklearn.linear_model import LinearRegression

model = LinearRegression()

model.fit(X_train, y_train)

predictions = model.predict(X_test)

print(predictions[:10])

from sklearn.metrics import mean_squared_error, r2_score

mse = mean_squared_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("Mean Squared Error:", mse)
print("R2 Score:", r2)

# Visualizations 

#1. Distribution of ratings and relationship with votes and cost
plt.figure(figsize=(8,5))
sns.histplot(data['Aggregate rating'], bins=20, kde=True)

plt.title("Distribution of Restaurant Ratings")
plt.xlabel("Rating")
plt.ylabel("Count")

plt.show()

#2. Scatter plot of votes vs ratings to see if there's a correlation

plt.figure(figsize=(8,5))
sns.scatterplot(x=data['Votes'], y=data['Aggregate rating'])

plt.title("Votes vs Rating")
plt.xlabel("Votes")
plt.ylabel("Rating")

plt.show()

#3. heatmap of feature correlations to see how votes and cost relate to ratings
plt.figure(figsize=(8,5))
sns.heatmap(data.corr(numeric_only=True), annot=True, cmap="coolwarm")

plt.title("Feature Correlation Heatmap")

plt.show()