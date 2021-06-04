import pandas as pd

something = [[1, "p", 2], [3, "t", 5], [6, "u", 10], [1, "p", 2], [4, "l", 9], [1, "t", 2], [3, "t", 5], [6, "c", 10], [1, "p", 2], [4, "l", 9]]
test = pd.DataFrame(something)
print(test)
test = test.drop_duplicates()
test.columns = ['id', 'state', 'level']
test = test.sort_values(by=['id'], ascending=True)
test_unique = test["id"].unique()


df_aslist = test.groupby(['id', 'level']).aggregate(lambda x: list(x)).reset_index()

df_aslist['state'] = df_aslist['state'].apply(lambda x: '-'.join(x))

print(df_aslist)

print(df_aslist[df_aslist['id'] == 1])
