import pandas as pd


df_d = {'League': ['Albania', 'Scotland', 'England'], 'DefDuels':[10,11,12], 'AerialDuels': [4., 5., 6.]}

df = pd.DataFrame(data=df_d)
print(df)