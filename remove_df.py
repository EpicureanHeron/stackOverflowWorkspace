import pandas as pd

data = ({"Year": [ 2020, 2019, 2020, "this is it?", 2019, 2020] ,
         "Sales Person": ["John", "Xiao", "Evelyn", "?", "Samantha", "Maria"],
         "Sales Budget": [20000, '?', 30000, 32000, 54000, 25000]})

df = pd.DataFrame(data=data)

print(df)

subset = df[(df.str.contains("?"))]
subset.head()

print(subset)