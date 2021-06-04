import pandas as pd

report=['A','B','C']
suffix='_US'

report2=[s + suffix for s in report]
print (report2) #result: ['A_US', 'B_US', 'C_US']

source = {'COL1': ['A','B','C'], 'COL2': ['D','E','F']}
dfsource=pd.DataFrame(source)
print(dfsource)

df_dict = {}
for i in report2:
    for x in report:
      new_key = x + i
      df_dict[new_key]=pd.DataFrame()
      df_dict[new_key]=dfsource.query('COL1==@x')

for item in df_dict.items():
    print(item)