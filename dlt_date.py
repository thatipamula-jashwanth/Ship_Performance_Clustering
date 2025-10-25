import pandas as pd

df = pd.read_csv('Ship_Performance_Dataset.csv')

drop_columns = ['Date']
df.drop(columns=drop_columns, inplace=True)

df.to_csv('Ship_Performance_Dataset.csv', index=False)

print('columns after dropping date column:')
print(df.columns)

