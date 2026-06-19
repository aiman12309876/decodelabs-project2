import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

print("\n" + "=" * 60)
print("   MODEL EVALUATION - PROJECT 2 TASK 2")
print("=" * 60)

data = {
    'Age': [25, 30, 22, 28, 35, 27, 40, 19, 33, 29, 45, 24, 31, 26, 38, 21, 34, 29, 32, 27],
    'Salary': [50000, 60000, 45000, 55000, 70000, 48000, 80000, 35000, 65000, 52000, 90000, 42000, 58000, 47000, 75000, 38000, 62000, 51000, 67000, 49000],
    'Experience': [2, 5, 1, 4, 8, 3, 12, 0, 6, 4, 15, 2, 7, 3, 10, 1, 8, 4, 9, 3],
    'Education_Score': [7, 8, 6, 9, 7, 8, 9, 5, 8, 7, 9, 6, 8, 7, 8, 6, 9, 7, 8, 7],
    'Purchased': ['No', 'Yes', 'No', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'No', 'Yes', 'No', 'Yes', 'No', 'Yes', 'No', 'Yes', 'No', 'Yes', 'No']
}

df = pd.DataFrame(data)

label_encoder = LabelEncoder()
df['Purchased_Encoded'] = label_encoder.fit_transform(df['Purchased'])

X = df[['Age', 'Salary', 'Experience', 'Education_Score']]
y = df['Purchased_Encoded']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("\n[1] Model Performance Metrics:")
print("-" * 60)
print(f"Accuracy:  {accuracy_score(y_test, y_pred) * 100:.2f}%")
print(f"Precision: {precision_score(y_test, y_pred) * 100:.2f}%")
print(f"Recall:    {recall_score(y_test, y_pred) * 100:.2f}%")
print(f"F1 Score:  {f1_score(y_test, y_pred) * 100:.2f}%")

print("\n[2] Confusion Matrix:")
print("-" * 60)
cm = confusion_matrix(y_test, y_pred)
print(cm)

print("\n[3] Interpretation:")
print("-" * 60)
tn, fp, fn, tp = cm.ravel()
print(f"True Negatives:  {tn}")
print(f"False Positives: {fp}")
print(f"False Negatives: {fn}")
print(f"True Positives:  {tp}")

print("\n" + "=" * 60)
print("   TASK 2 COMPLETE")
print("=" * 60)