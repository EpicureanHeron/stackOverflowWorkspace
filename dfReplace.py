#h ttps://stackoverflow.com/questions/67416681/how-to-replace-a-exact-matching-string-in-pandas-string-column

# original question

import pandas as pd

data = {"Column1" : ["Income recorded on books this year not included on Schedule K, lines 1 through 11 (itemize):",
                     "a Tax-exempt interest $ Statement #36",
                     "Statement #36"],
        "Column2" : [254, 258, 356]}

df = pd.DataFrame(data)


df['Key'] = df['Column1'].str.replace(r'\$\ Statement #36', '', regex=True)

print(df['Key'])