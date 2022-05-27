def remove_comma(s):
    return float(s.replace(',', ''))



import pandas as pd

df = pd.read_csv("ups_ex.csv")

file = open("final.csv", "w")

for col in df.columns:
    file.write(str(col) + ",")
file.write("\n")


for rows in df.itertuples():
    count = 0
    for cols in rows:
        if count == 0:
            count += 1
            continue
        cols = remove_comma(str(cols))
        file.write(str(cols) + ",")
    file.write("\n")