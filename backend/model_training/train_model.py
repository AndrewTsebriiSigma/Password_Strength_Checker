import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import joblib

data= pd.read_csv(r"C:\Users\andri\Desktop\Lab_Week3\week 8\Password_Strength_Checker\backend\model_training\Updated_Password_Dataset.csv")
df = pd.DataFrame(data)
shuffled_df = shuffle(df)

shuffled_df = shuffled_df.drop(columns=['passwords'])

def normalizer(df):

    normalized_df = (df - df.min()) / (df.max() - df.min())
    for i in normalized_df.columns:
        df[i] = normalized_df[i]

    return df

shuffled_df_normalized = normalizer(shuffled_df)

features = ['upperCase', 'Long_Length', 'letter_count', 'digit_count', 'non_repeating', 'symbol_count']
X = shuffled_df_normalized[features]
y = shuffled_df_normalized['strength']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size=0.3)

model = LogisticRegression(C=1.0, random_state=42)
model.fit(X_train, y_train)
predicted = model.predict(X_test)
print(f'Accuracy Score: {accuracy_score(y_test, predicted)}')

cv_scores = cross_val_score(model, X_scaled, y, cv=5, scoring='accuracy')
print(f'Cross-Validation Accuracy Scores: {cv_scores}')
print(f'Mean CV Accuracy: {cv_scores.mean()}')

#Saving the model
joblib.dump(model, 'password_strength_model.pkl')