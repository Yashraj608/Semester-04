import numpy as nm
import matplotlib.pyplot as mtp
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import numpy as np

nm.random.seed(42)

n = 200

df = pd.DataFrame({
    'CustomerID': range(1, n+1),
    'Gender': nm.random.choice(['Male', 'Female'], n),
    'Age': nm.random.randint(18, 70, n),
    'Annual Income (k$)': nm.random.randint(15, 150, n),
    'Spending Score (1-100)': nm.random.randint(1, 100, n)
})

df = pd.get_dummies(df, columns=['Gender'])

X = df.drop(columns=['CustomerID'])

age = X[['Age']]
other_features = X.drop(columns=['Age'])

scaler = StandardScaler()
other_scaled = scaler.fit_transform(other_features)

X_scaled = np.concatenate([age.values, other_scaled], axis=1)

kmeans_no_scaling = KMeans(n_clusters=5, init='k-means++', random_state=42)
clusters_no_scaling = kmeans_no_scaling.fit_predict(X)

kmeans_scaling = KMeans(n_clusters=5, init='k-means++', random_state=42)
clusters_scaling = kmeans_scaling.fit_predict(X_scaled)

df['cluster_no_scaling'] = clusters_no_scaling
df['cluster_with_scaling'] = clusters_scaling

print(df[['CustomerID', 'cluster_no_scaling', 'cluster_with_scaling']])

mtp.scatter(df['Annual Income (k$)'], df['Spending Score (1-100)'], c=clusters_no_scaling)
mtp.title('Clusters without Scaling')
mtp.xlabel('Annual Income')
mtp.ylabel('Spending Score')
mtp.show()

mtp.scatter(df['Annual Income (k$)'], df['Spending Score (1-100)'], c=clusters_scaling)
mtp.title('Clusters with Scaling')
mtp.xlabel('Annual Income')
mtp.ylabel('Spending Score')
mtp.show()