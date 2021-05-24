# https://stackoverflow.com/questions/67487599/remove-rows-from-a-data-frame-found-in-another-df/67487699#67487699

import pandas as pd

df1 = pd.DataFrame({
    "name": ["Peter", "John", "Jack", "Mark", "Adam", "Mike", "Aaron", "Mike"],
    "age": [25, 34, 58, 29, 42, 39, 48, 24],
})

df2 = pd.DataFrame({
    "name": ["Mark", "Jack", "Adam", "Mike"],
    "age": [29, 58, 42, 39],
    "is_funny": [False, True, True, False],
})

df3 = df2.merge(df1, on=['name','age'], how='outer', indicator=True)\
   .query('_merge == "right_only"').reindex(df1.columns, axis=1)

print(df3)