
import pandas as pd

source = {'ID': ['MEXU ','RFGT','RFGT', 'OJKU', 'TYED'], 'TYPE': ['DOL','DOL','DOL', 'RET', 'NaN'], 'HEIGHT': ['NaN', 140, 'NaN', 90, 'NaN'], 'KG': [40, 47, 'NaN', 'NaN', 'NaN']}

df = pd.DataFrame(data=source)


grouped = df.groupby('ID', as_index=False).first()

print(grouped)