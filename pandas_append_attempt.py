import pandas as pd

df_d = {'Element':['customer full name','full name','name','religion','account number','lgbt','lgbt identity'],
"days_between": [0, 8, 15, 0, 55, 6, 5]}

df_b = {'Element':['customer full name','full name','name','religion','account number','lgbt','lgbt identity'],
"days_between": [0, 8, 15, 0, 55, 6, 5]}

df = pd.DataFrame(data=df_d)

newDF = pd.DataFrame(data=df_b)

print(df.append([df, pd.DataFrame(newDF)], ignore_index = False))

df = df.append(newDF, ignore_index = False)
print(df)