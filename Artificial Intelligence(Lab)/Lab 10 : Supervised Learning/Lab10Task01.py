import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error , mean_absolute_error , median_absolute_error , r2_score
from sklearn.preprocessing import LabelEncoder
np.random.seed(42)
n = 200
data = pd.DataFrame(
    {
        "Study_Hours": np.random.normal(5, 2, n),
        "Attendance": np.random.normal(80, 10, n),
        "Previous_grade": np.random.normal(70, 15, n),
        "internet_usage": np.random.normal(3, 1.5, n),
        "participation": np.random.choice(["Low","Medium","High"], n),

    }
)

participation_map = {
    "Low": 0,
    "Medium": 5,
"High": 10,}


data["Final_Score"] =(
    data["Study_Hours"]*5 +
    data["Attendance"]*0.3 +
    data["Previous_grade"]*0.4 +
    data["internet_usage"]* -2 +
    data["participation"].map(participation_map) +
    np.random.normal(0, 5, n)
)

data["Attendance"].fillna(data["Attendance"].mean(), inplace=True)
data["Study_Hours"].fillna(data["Study_Hours"].mean(), inplace=True)

le = LabelEncoder()
data["participation"] = le.fit_transform(data["participation"])

x= data.drop("Final_Score", axis=1)
y = data["Final_Score"]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

model = LinearRegression()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)
mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print("MSE :",mse)
print("MAE :",mae)
print("R2 Score :",r2)


new_student = pd.DataFrame(
    [
        {
            "Study_Hours":6,
            "Attendance":85,
            "Previous_grade":75,
            "internet_usage":2,
            "participation":2,

        }
    ]
)
new_student["participation"] = le.fit_transform(new_student["participation"])
prediction = model.predict(new_student)