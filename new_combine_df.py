import pandas as pd

df = pd.DataFrame({'Col_1': ['A', 'B', 'C'],
                   'Col_2': ['D', 'E', 'F'],
                   'Col_one':['G', 'H', 'I'],})

df2 = pd.DataFrame()

df2['Col_1'] = pd.concat([df['Col_1'], df['Col_one']], axis = 0)

df2 = df2.reset_index()

df2 = df2.drop('index', axis =1)

df2['Col_2'] = df['Col_2']

df2['Col_2'] = df2['Col_2'].fillna('-')

print(df2)