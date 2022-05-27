# Basic Details 

name = "DTDC"
ddp_frdm = 730
fixed_cost = 0
covid_surcharge = 10
fuel_surcharge = 10
exchange_surcharge = 0
residential_delivery_surcharge = 170
emergency_situation_surcharge = 0
peak_surcharge = 0

countries = []

import pandas as pd

file = pd.read_csv("~/Desktop/Goglocal/Logistics/data/aramex/zones.csv")

for rows in file.itertuples():
    country = rows[1]
    countries.append(country)


import psycopg2

conn = psycopg2.connect("dbname=logistics user=postgres password=postgres")
conn.autocommit = True
cursor = conn.cursor()

cursor.execute("INSERT INTO logistic_partners (name, ddp_frdm, fixed_cost) VALUES (%s, %s, %s)", (name, ddp_frdm, fixed_cost))

cursor.execute("SELECT * FROM logistic_partners WHERE name = %s", (name,))
logistic_partner_id = cursor.fetchone()[0]


for country in countries:
    cursor.execute(
        "INSERT INTO add_on_charges (country, logistic_partner, covid_surcharge, fuel_surcharge, exchange_surcharge, residential_delivery_surcharge, emergency_situation_surcharge, peak_surcharge) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (country, logistic_partner_id, covid_surcharge, fuel_surcharge, exchange_surcharge, residential_delivery_surcharge, emergency_situation_surcharge, peak_surcharge))
