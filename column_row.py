import pandas as pd

date_dict= {'code': ['PUT123', 'MAT456', 'CAT123'], 'Desc': ['Deduct', 'Coin', 'Copay'], 'STC': ['30, 47, 57', '30, 54, 27', '8, 1, 9']
       }

df = pd.DataFrame(data=date_dict)

df2 = (df.loc[df['STC'].str.contains(r'30', na=True)])

print(df2['STC'])

