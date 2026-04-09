import pandas as pd

df = pd.read_csv(r"C:\Users\brian\Downloads\data.csv")

new_df=df.fillna(130, inplace=True)
print(new_df.to_string())


import matplotlib

print(matplotlib.__version__)