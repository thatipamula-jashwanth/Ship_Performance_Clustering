import pandas as pd
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import silhouette_score
import pickle
import numpy as np

df = pd.read_csv('ship_performance_encoded.csv') 

for col in df.columns:
    if df[col].dtype == 'bool':
        df[col] = df[col].astype(float)

df = df.fillna(0)  
df = df.replace([np.inf, -np.inf], 0)


n_clusters = 2
hc = AgglomerativeClustering(n_clusters=n_clusters, linkage='average')
clusters = hc.fit_predict(df)


df['Cluster'] = clusters

sil_score = silhouette_score(df.drop('Cluster', axis=1), clusters)
print(f"Silhouette Score for {n_clusters} clusters: {sil_score:.3f}")

with open('ship_performance_clustered.pkl', 'wb') as f:
    pickle.dump(df, f)

print("Clustering completed and saved as 'ship_performance_clustered.pkl'")
