import pandas as pd 

df = pd.read_csv('Ship_Performance_Dataset.csv')

categorical_columns = df.select_dtypes(include=['object', 'category']).columns

print('categoorical_columns')
print(list(categorical_columns))
print('\nTotal:', len(categorical_columns))

print('\n unique values in categorical columns:')
for col in categorical_columns:
    print(f'{col}: {df[col].nunique()}unique valus')