import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_score, recall_score, roc_auc_score, confusion_matrix, classification_report
from imblearn.over_sampling import SMOTE
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)

print("\n" + "=" * 60)
print("   FRAUD DETECTION PIPELINE - SUPERVISED LEARNING")
print("=" * 60)

print("\n[1] Creating Sample Dataset...")

n = 2000
fraud_ratio = 0.05
n_fraud = int(n * fraud_ratio)
n_legit = n - n_fraud

amount = np.random.gamma(shape=2, scale=200, size=n)
amount = np.clip(amount, 1, 10000)

location = np.random.choice(['New York', 'London', 'Dubai', 'Singapore', 'Tokyo'], n)
device = np.random.choice(['Mobile', 'Desktop', 'Tablet'], n)
age = np.random.randint(18, 70, n)
balance = np.random.randint(100, 10000, n)

fraud = np.zeros(n)
fraud_indices = np.random.choice(range(n), n_fraud, replace=False)
fraud[fraud_indices] = 1

fraud[fraud_indices] = 1
amount[fraud_indices] = amount[fraud_indices] * np.random.uniform(1.5, 3.0, n_fraud)
location[fraud_indices] = np.random.choice(['New York', 'London', 'Dubai', 'Singapore', 'Tokyo'], n_fraud)
device[fraud_indices] = np.random.choice(['Mobile', 'Desktop', 'Tablet'], n_fraud)

data = pd.DataFrame({
    'Amount': amount,
    'Age': age,
    'Balance': balance,
    'Location': location,
    'Device': device,
    'Fraud': fraud
})

print(f"Total Transactions: {len(data)}")
print(f"Legitimate: {len(data[data['Fraud'] == 0])}")
print(f"Fraudulent: {len(data[data['Fraud'] == 1])}")

print("\n[2] Data Preprocessing...")

data_encoded = pd.get_dummies(data, columns=['Location', 'Device'], drop_first=True)

X = data_encoded.drop('Fraud', axis=1)
y = data_encoded['Fraud']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print(f"Training set: {len(X_train)} rows")
print(f"Testing set: {len(X_test)} rows")

print("\n[3] Handling Class Imbalance with SMOTE...")
smote = SMOTE(random_state=42)
X_train_resampled, y_train_resampled = smote.fit_resample(X_train_scaled, y_train)

print(f"After SMOTE - Legitimate: {sum(y_train_resampled == 0)}")
print(f"After SMOTE - Fraudulent: {sum(y_train_resampled == 1)}")

print("\n[4] Training Models...")

models = {
    'Logistic Regression': LogisticRegression(max_iter=1000),
    'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42)
}

results = {}

for name, model in models.items():
    model.fit(X_train_resampled, y_train_resampled)
    y_pred = model.predict(X_test_scaled)
    y_proba = model.predict_proba(X_test_scaled)[:, 1]

    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    roc_auc = roc_auc_score(y_test, y_proba)

    results[name] = {
        'Precision': precision,
        'Recall': recall,
        'ROC-AUC': roc_auc,
        'Model': model
    }

    print(f"\n{name}:")
    print(f"  Precision: {precision:.4f}")
    print(f"  Recall: {recall:.4f}")
    print(f"  ROC-AUC: {roc_auc:.4f}")

print("\n[5] Confusion Matrices:")
for name, result in results.items():
    model = result['Model']
    y_pred = model.predict(X_test_scaled)
    cm = confusion_matrix(y_test, y_pred)
    print(f"\n{name}:")
    print(cm)

print("\n[6] Best Model:")
best_model = max(results.keys(), key=lambda x: results[x]['ROC-AUC'])
print(f"Best performing model: {best_model}")
print(f"ROC-AUC: {results[best_model]['ROC-AUC']:.4f}")
print(f"Precision: {results[best_model]['Precision']:.4f}")
print(f"Recall: {results[best_model]['Recall']:.4f}")

print("\n[7] Feature Importance (Random Forest):")
rf_model = results['Random Forest']['Model']
feature_importance = pd.DataFrame({
    'Feature': X.columns,
    'Importance': rf_model.feature_importances_
}).sort_values('Importance', ascending=False)
print(feature_importance.head(10))

print("\n" + "=" * 60)
print("   TASK 9 COMPLETE")
print("=" * 60)