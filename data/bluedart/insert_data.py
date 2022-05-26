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

df = pd.read_csv("/home/jayash/Desktop/Goglocal/Logistics/data/bluedart/bluedart.csv")


cursor.execute("SELECT * FROM logistic_partners WHERE name = %s", ("Bluedart",))
logistic_partner_id = cursor.fetchone()[0]


weights = []

for rows in df:
    weights.append(rows[1])

count = 2

for rows in df:
    weight_lower_range = rows[1]
    weight_upper_range = weights[count]
    count+=1
    
    for i in range(1, 12):
        countries = zone_country_relation[i]
        for country in countries:
            cost = rows[i+1]
            cursor.execute(
                "INSERT INTO logistics (country, price, weight_upper_range, weight_lower_range, partner_id) VALUES (%s, %s, %s, %s, %s)", (country, cost, weight_upper_range, weight_lower_range, logistic_partner_id))

