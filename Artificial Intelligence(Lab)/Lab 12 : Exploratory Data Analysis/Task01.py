import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

df = pd.read_csv("house_prices_practice.csv")

print(df.head())
print(df.shape)
print(df.columns)

num_cols = df.select_dtypes(include=np.number).columns
cat_cols = df.select_dtypes(exclude=np.number).columns

print("Numerical:", num_cols)
print("Categorical:", cat_cols)

print(df.isnull().sum())

for col in num_cols:
    df[col] = df[col].fillna(df[col].median())

for col in cat_cols:
    df[col] = df[col].fillna(df[col].mode()[0])

threshold = len(df) * 0.5
df = df.dropna(thresh=threshold, axis=1)

plt.hist(df['SalePrice'])
plt.title('SalePrice Distribution')
plt.show()

plt.boxplot(df['SalePrice'])
plt.title('SalePrice Boxplot')
plt.show()

plt.hist(df['GrLivArea'])
plt.title('GrLivArea Distribution')
plt.show()

plt.boxplot(df['GrLivArea'])
plt.title('GrLivArea Boxplot')
plt.show()

corr = df.corr(numeric_only=True)
print(corr['SalePrice'].sort_values(ascending=False))

plt.scatter(df['GrLivArea'], df['SalePrice'])
plt.xlabel('GrLivArea')
plt.ylabel('SalePrice')
plt.show()

df.groupby('OverallQual')['SalePrice'].mean().plot(kind='bar')
plt.show()

top_features = corr['SalePrice'].abs().sort_values(ascending=False).head(6)
print(top_features)

sns.heatmap(corr, cmap='coolwarm')
plt.show()

df['HouseAge'] = df['YrSold'] - df['YearBuilt']

if 'Id' in df.columns:
    df = df.drop(columns=['Id'])

df = pd.get_dummies(df, drop_first=True)

X = df.drop(columns=['SalePrice'])
y = df['SalePrice']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print("MAE:", mae)
print("RMSE:", rmse)
print("R2 Score:", r2)