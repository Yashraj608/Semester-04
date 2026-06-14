import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.preprocessing import LabelEncoder

np.random.seed(42)
n= 200
data = pd.DataFrame(
        {
           "Income": np.random.normal(50000, 10000, n),
            "Employment_status": np.random.choice(["Employed", "Not employed","Self-Employed"], n),
            "Credit_score": np.random.normal(650, 50, n),
            "Loan_amount": np.random.normal(20000,5000, n),
            "Marital_status": np.random.choice(["Single","Married"],n),
        }
)

data["Loan_Approved"] = (
(data["Income"] > 45000) & (data["Credit_score"] > 600)
).astype(int)

data.loc[np.random.randint(0,n,10),"Income"] = np.nan
data["Income"]= data["Income"].fillna(data["Income"].mean())

le_emp = LabelEncoder()
le_mar = LabelEncoder()

data["Employment_status"] = le_emp.fit_transform(data["Employment_status"])
data["Marital_status"] = le_mar.fit_transform(data["Marital_status"])

x = data.drop("Loan_Approved", axis=1)
y = data["Loan_Approved"]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

model = DecisionTreeClassifier()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)
print("Classification Report :")
print(classification_report(y_test, y_pred))
print("Confusion Matrix :",confusion_matrix(y_test, y_pred))

new_applicant = pd.DataFrame(
    [
        {
            "Income": 60000,
            "Employment_status": le_emp.transform(["Employed"])[0],
            "Credit_score": 700,
            "Loan_amount": 15000,
            "Marital_status": le_mar.transform(["Married"])[0]
        }
    ]
)

prediction = model.predict(new_applicant)
print("Loan Approval Prediction",prediction[0])