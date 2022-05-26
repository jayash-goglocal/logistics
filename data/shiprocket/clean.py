def remove_comma(s):
    return float(s.replace(',', ''))


from os import remove
import pandas as pd

file = pd.read_csv("shiprocket.csv")

new_file = open("final.csv", "w")

for cols in file.columns:
    cols = cols.strip()
    new_file.write(cols + ",")
new_file.write("\n")

for rows in file.itertuples():
    
    count = 0
    for cols in rows:
        if count == 0:
            count += 1
            continue
    
        cols = remove_comma(str(cols))
        new_file.write(str(cols) + ",")
    new_file.write("\n")