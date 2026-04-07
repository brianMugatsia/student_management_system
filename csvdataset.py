import pandas as pd

df = pd.read_csv(r"C:\Users\brian\Downloads\data.csv")

print(df.to_string())
print(pd.options.display.max_rows)