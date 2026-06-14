import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler, LabelEncoder

np.random.seed(42)
n = 200

data = pd.DataFrame({
    "Monthly_Charges": np.random.normal(70, 20, n),
    "Contract_Type": np.random.choice(["Month-to-month", "One year", "Two year"], n),
    "Tenure": np.random.randint(1, 72, n),
    "Internet_Service": np.random.choice(["DSL", "Fiber", "None"], n),
    "Support_Calls": np.random.randint(0, 10, n)
})

data["Churn"] = (
    (data["Monthly_Charges"] > 80) &
    (data["Support_Calls"] > 5) &
    (data["Tenure"] < 12)
).astype(int)


data.loc[np.random.randint(0,n,10), "Monthly_Charges"] = np.nan
data["Monthly_Charges"] = data["Monthly_Charges"].fillna(data["Monthly_Charges"].mean())


data["Monthly_Charges"] = np.clip(data["Monthly_Charges"], 10, 150)


le_contract = LabelEncoder()
le_internet = LabelEncoder()

data["Contract_Type"] = le_contract.fit_transform(data["Contract_Type"])
data["Internet_Service"] = le_internet.fit_transform(data["Internet_Service"])


X = data.drop("Churn", axis=1)
y = data["Churn"]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


x_train, x_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)


r = RandomForestClassifier()
r.fit(x_train, y_train)

svm_model = SVC(kernel="linear")
svm_model.fit(x_train, y_train)

y_pred = r.predict(x_test)

print("Classification Report:\n", classification_report(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))


importance = r.feature_importances_
for i, col in enumerate(X.columns):
    print(f"{col}: {importance[i]}")


new_customer = pd.DataFrame([{
    "Monthly_Charges": 90,
    "Contract_Type": le_contract.transform(["Month-to-month"])[0],
    "Tenure": 5,
    "Internet_Service": le_internet.transform(["Fiber"])[0],
    "Support_Calls": 7
}])

new_customer_scaled = scaler.transform(new_customer)
prediction = r.predict(new_customer_scaled)

print("Churn Prediction:", prediction[0])