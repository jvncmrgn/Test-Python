import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Sample historical price data
data = {
    'Price': [100, 101, 102, 103, 102, 101, 100, 99, 98, 97],
}

df = pd.DataFrame(data)

# Create a binary label: 1 for price increase, 0 for price decrease
df['Label'] = np.where(df['Price'].diff() > 0, 1, 0)

# Features and labels
X = df[['Price']].values
y = df['Label'].values

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train a logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print(f'Accuracy: {accuracy}')
print(f'Classification Report:\n{report}')
