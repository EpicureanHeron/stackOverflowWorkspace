# I am trying to put together the following data frame in pandas. Initially I have 3 columns. I want to create a new column called "Status" based on condition, if Days_between > 7 then "New course" else "Existing Course" for particular ID

# I tried groupby with if else condition but could not put the logic correct. Any help would be appreciated.


# df 
import pandas as pd 

df_d = {'Element':['customer full name','full name','name','religion','account number','lgbt','lgbt identity'],
"days_between": [0, 8, 15, 0, 55, 6, 5]}

df = pd.DataFrame(data=df_d)

df['status'] = df['days_between'].apply(lambda x: 'New course' if x > 7 else 'Existing Course')


print(df)