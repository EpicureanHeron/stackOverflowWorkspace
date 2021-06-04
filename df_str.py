import pandas as pd

df = pd.DataFrame(columns= ['Name', 'Attr', 'Description'])
df = df.append({'Name':'Water'}, ignore_index=True)

print(df["Name"].str.contains(df["Name"][0]))