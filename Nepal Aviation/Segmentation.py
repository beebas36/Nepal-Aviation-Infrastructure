from sklearn.cluster import KMeans
import pandas as pd

df = pd.read_csv("customer_data.csv")
X = df[['age', 'annual_income', 'spending_score']]

kmeans = KMeans(n_clusters=4, random_state=42)
df['segment'] = kmeans.fit_predict(X)
