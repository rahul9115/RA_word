import pandas as pd
old_df=pd.read_csv("old_filings.csv")
l=[old_df]
df=pd.read_csv("filings.csv")
l.append(df)
merged=pd.concat(l)
merged.to_csv("filings_updated.csv")