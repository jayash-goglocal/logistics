def remove_comma(s):
    return float(s.replace(',', ''))


import pandas as pd

import psycopg2

conn = psycopg2.connect("dbname=logistics user=postgres password=postgres")
conn.autocommit = True
cursor = conn.cursor()


file = pd.read_csv("/home/jayash/Desktop/Goglocal/Logistics/data/aramex/zones.csv")

zone_country_relation = {}

for rows in file.itertuples():
    if rows[2] not in zone_country_relation:
        zone_country_relation[rows[2]] = []

    zone_country_relation[rows[2]].append(rows[1])

df = pd.read_csv("/home/jayash/Desktop/Goglocal/Logistics/data/aramex/aramex.csv")


cursor.execute("SELECT * FROM logistic_partners WHERE name = %s", ("UPS Economy",))
logistic_partner_id = cursor.fetchone()[0]


weights = []

for rows in df.itertuples():
    weights.append(rows[1])

count = 1

for rows in df.itertuples():
    weight_lower_range = rows[1]

    try:
        weight_upper_range = weights[count]
    except:
        weight_upper_range = 10000
    
    count+=1
    
    for i in range(1, 10):
        countries = zone_country_relation[i]
        for country in countries:
            cost = remove_comma(str(rows[i+1]))
            cursor.execute(
                "INSERT INTO logistics (country, price, weight_upper_range, weight_lower_range, partner_id) VALUES (%s, %s, %s, %s, %s)", (country, cost, weight_upper_range, weight_lower_range, logistic_partner_id))

