import pandas as pd
import numpy as np

df = pd.DataFrame({"A":np.array([1,2,3,4]),"B":np.array([1,2,3,4])})
df_mean = df.mean(axis=0)
print(df_mean)

