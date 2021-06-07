import pandas as pd
df = pd.DataFrame ([['Europe', 10000000, 'Product Charge', 1000], 
                    ['Europe', 10001000, 'Product Charge', 1000], 
                    ['Europe', 10001000, 'Discount', -500],
                    ['Latam', 10002000, 'Product Charge', 0],
                    ['Latam', 10003000, 'Product Charge', 1000],
                    ['Latam', 10003000, 'Discount', -1000],
                    ['Europe', 10004000, 'Product Charge', 500],
                    ['Europe', 10004000, 'Discount', -500],
                    ['Europe', 10005000, 'Product Charge', 500],
                    ['Europe', 10005000, 'Discount', 495],
                    ['Latam', 10006000, 'Product Charge', 0],])

df.columns = ['Division', 'Invoice', 'Transactions', 'Amount']


new_df = df.where(['Amount'] == 0)

print(new_df)