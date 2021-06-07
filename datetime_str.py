import pandas as pd

date_dict= {'date': ['2015-08-26 10:24:48.127', '2015-08-26 10:26:41.000',
       '2015-08-26 10:27:52.000', '2015-08-26 10:18:11.000',
       '2015-08-26 10:21:39.000', '2015-08-26 10:23:05.000']}

df = pd.DataFrame(data=date_dict)

df['date']= pd.to_datetime(df['date'], format="%Y-%m-%d %H:%M:%S.%f")

print(df['date'])