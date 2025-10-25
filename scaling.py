import pandas as pd
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('ship_performance_encoded.csv')

features = df.columns.tolist()
scaler = StandardScaler()

X_scaled = scaler.fit_transform(df[features])

df_scaled = pd.DataFrame(X_scaled, columns=features)
print(df_scaled.head(5))

