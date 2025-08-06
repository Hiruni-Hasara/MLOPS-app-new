import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

# Load dataset
url = "https://raw.githubusercontent.com/Hiruni-Hasara/hosted-datasets/refs/heads/main/heart.csv"
df = pd.read_csv(url)

# Encode categorical variables
for col in df.select_dtypes(include='object'):
    df[col] = LabelEncoder().fit_transform(df[col])

X = df.drop("HeartDisease", axis=1)
y = df["HeartDisease"]

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# Save model
joblib.dump(model, "model.pkl")
