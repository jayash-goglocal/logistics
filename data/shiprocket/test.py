import pandas as pd

file = pd.read_csv("final.csv")

print(len(file.columns))

for rows in file.itertuples():
    print(len(rows))