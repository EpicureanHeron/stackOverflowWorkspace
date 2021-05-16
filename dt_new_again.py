import pandas as pd 

data = {
    'city': ['São Paulo', 'Rio', 'Recife'],
    'area(m2)': [90, 120, 60],
    'Rooms': [3, 2, 4],
    'Bathrooms': [2, 3, 3],
    'animal': ['accept', 'do not accept', 'accept'],
    'rent($)': [2000, 3000, 800]}

df = pd.DataFrame(
    data,
    columns=['city', 'area(m2)', 'Rooms', 'Bathrooms', 'animal', 'rent($)'])

df_filtered = df[(df['Rooms'] <= 2) & (df['Bathrooms'] <= 2)]

print(df_filtered)

