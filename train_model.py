import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report
import joblib

# Load your dataset
df = pd.read_csv("train.csv")

# Drop missing values (or use imputation if preferred)
df.dropna(inplace=True)

# Categorical columns to encode
label_cols = [
    "Gender", "Married", "Dependents", "Education",
    "Self_Employed", "Property_Area", "Loan_Status"
]

# Encode categoricals using LabelEncoder
encoders = {}
for col in label_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    encoders[col] = le

# Features and target (note: no Loan_Type column here)
X = df[[
    "LoanAmount", "Gender", "Married", "Dependents",
    "Education", "Self_Employed", "ApplicantIncome",
    "CoapplicantIncome", "Credit_History", "Property_Area"
]]
y = df["Loan_Status"]

# Split into train/test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print("\n📊 Classification Report:\n")
print(classification_report(y_test, y_pred))

# Save model
joblib.dump(model, "loan_model.pkl")
print("\n✅ Model saved as 'loan_model.pkl'")