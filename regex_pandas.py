import pandas as pd

df = pd.DataFrame()

df['col'] = ['text', 'Texts', 'Text-Pro', 'Text;Nothing', 'Pro', 'pro', 'Pros', 'Nothing']

masking = df['col'].str.contains(r'(Text|text)|(Pro|pro)')

print(masking)