import pandas as pd 

df = pd.DataFrame({
    'ID': range(1, 4),
    'col1': [10, 5, 10],
    'col2': [15, 10, 15],
    'col3': [10, 15, 15],
    'total': [35, 30, 40]
})

df['col1'] = (df['col1']/df['total']).mul(100).round(2).astype(str).add('%')
df['col2'] = (df['col2']/df['total']).mul(100).round(2).astype(str).add('%')
df['col3'] = (df['col3']/df['total']).mul(100).round(2).astype(str).add('%')
df['total'] = (df['total']/df['total']).mul(100).round(2).astype(str).add('%')


print(df)