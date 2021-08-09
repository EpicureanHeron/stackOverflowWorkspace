import pandas as pd

date_dict= {'Store number': ['A', 'B', 'C'], 'Week 14': [2, 1, 2], 'Week 15': [4,2,2], 'Week 16' : [4,2,2]
       }

df = pd.DataFrame(data=date_dict)

df2 = pd.read_excel('test.xlsx', sheet_name="All Sales")

df2 = df2.drop('Week 14', axis = 1)

df2 = df2.merge(df, left_on='Store number', right_on ='Store number')


df2.to_excel('test.xlsx', index=False, sheet_name='All Sales')
