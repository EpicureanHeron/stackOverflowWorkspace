import pandas as pd

df1 = pd.DataFrame({'period':['2021-02'], 'customer':['A'], 'product':['Apple'], 'sales_flag': ['Yes']})

df2 = pd.DataFrame({'period':['2021-03', '2021-04', '2021-04'], 'customer':['A', 'A', 'A'], 'product':['Banana', 'Apple', 'Tangerine'], 'feedback_flag': ['Yes', 'Yes', 'No']})

df3 = pd.merge(df1, df2, on = ['period', 'customer',  'product'], how = 'inner')

print(df3)