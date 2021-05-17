import pandas as pd
report=['A','B','C']
df_dict = {}
for i in report:
    df_dict[i]=pd.DataFrame()

print(df_dict['A'])
print(df_dict['B'])
print(df_dict['C'])