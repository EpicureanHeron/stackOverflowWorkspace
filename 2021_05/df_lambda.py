import pandas as pd


df_d = {'League': ['Albania', 'Scotland', 'England'], 'DefDuels':[10,11,12], 'AerialDuels': [4., 5., 6.]}

df = pd.DataFrame(data=df_d)


England_row = df.loc[df['League']=='England']

England_value = England_row['DefDuels'].values[0]

df['New Column'] = df['DefDuels'].apply(lambda x:  England_value * x )

print(df)

df.loc[2,'New Column'] = 'N/A'

print(df)