import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('Ship_Performance_Dataset.csv')


categorical_columns = df.select_dtypes(include=['object', 'category']).columns.tolist()
print("Categorical columns detected:", categorical_columns)

low_card = [col for col in categorical_columns if df[col].nunique() <= 10]
high_card = [col for col in categorical_columns if df[col].nunique() > 10]

print("Low-cardinality columns (One-Hot Encoding):", low_card)
print("High-cardinality columns (Label Encoding):", high_card)

df = pd.get_dummies(df, columns=low_card, drop_first=True)

for col in high_card:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])

print("\nColumns after mixed encoding:")
print(df.columns)

df.to_csv('ship_performance_encoded.csv', index=False)
