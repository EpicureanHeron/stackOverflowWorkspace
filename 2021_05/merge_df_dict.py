import pandas as pd
main_df = pd.DataFrame(columns=['ID', 'Data1', 'Data2'], data=[['123', '1', '2'], ['456', '1', '2'], ['789', '1', '2']])

other_df = pd.DataFrame(columns=['RawData'], data=[['123XXX FooBar'], ['456XXX MooCar']])

other_df['prefix'] = other_df['RawData'].str.slice(0, 3)

merged_df = main_df.merge(other_df, left_on = 'ID', right_on='prefix', how='left')

merged_df = merged_df.drop(columns='prefix')

print(merged_df)