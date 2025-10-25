import pandas as pd
import numpy as np
from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt


df_scaled = pd.read_csv('ship_performance_encoded.csv') 


df_scaled = df_scaled.astype(float)


df_scaled = df_scaled.fillna(0)            
df_scaled = df_scaled.replace([np.inf, -np.inf], 0) 

linked = linkage(df_scaled, method='ward') 

plt.figure(figsize=(12, 6))
dendrogram(linked, truncate_mode='level', p=20)  
plt.title("Dendrogram for Ship Performance")
plt.xlabel("Samples")
plt.ylabel("Distance")
plt.show()
