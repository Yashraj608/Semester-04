import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans


np.random.seed(42)

n_students = 100

df = pd.DataFrame({
    'student_id': range(1, n_students + 1),
    'GPA': np.round(np.random.uniform(2.0, 4.0, n_students), 2),
    'study_hours': np.random.randint(5, 40, n_students),
    'attendance_rate': np.random.randint(50, 100, n_students)
})

print("Generated Dataset Preview:")
print(df.head())


X = df[['GPA', 'study_hours', 'attendance_rate']]


scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


inertia = []

for k in range(2, 7):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_scaled)
    inertia.append(kmeans.inertia_)


plt.figure()
plt.plot(range(2, 7), inertia, marker='o')
plt.title("Elbow Method for Optimal K")
plt.xlabel("Number of Clusters (K)")
plt.ylabel("Inertia")
plt.show()


optimal_k = 3

kmeans = KMeans(n_clusters=optimal_k, random_state=42)
df['cluster'] = kmeans.fit_predict(X_scaled)

# 8. Final Dataset Output
print("\nFinal Dataset with Cluster Labels:")
print(df[['student_id', 'cluster']])


plt.figure()
plt.scatter(df['study_hours'], df['GPA'], c=df['cluster'])

plt.title("Student Clusters based on Study Hours and GPA")
plt.xlabel("Study Hours")
plt.ylabel("GPA")

plt.show()