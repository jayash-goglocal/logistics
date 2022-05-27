import psycopg2


conn = psycopg2.connect("dbname=logistics user=postgres password=postgres")
conn.autocommit = True
cursor = conn.cursor()



cursor.execute("CREATE TABLE logistic_partners (id BIGSERIAL PRIMARY KEY NOT NULL, name TEXT NOT NULL, ddp_frdm NUMERIC (5, 2), fixed_cost NUMERIC (5, 2))")
cursor.execute("CREATE TABLE add_on_charges (id BIGSERIAL PRIMARY KEY NOT NULL, country TEXT NOT NULL, logistic_partner BIGINT REFERENCES logistic_partners(id) NOT NULL, covid_surcharge NUMERIC (5, 2), fuel_surcharge NUMERIC (5, 2), exchange_surcharge NUMERIC (5, 2), residential_delivery_surcharge NUMERIC (5, 2), emergency_situation_surcharge NUMERIC (5, 2), peak_surcharge NUMERIC (5, 2))")
cursor.execute("CREATE TABLE logistics (id BIGSERIAL PRIMARY KEY NOT NULL, country TEXT NOT NULL, price NUMERIC NOT NULL, weight_upper_range NUMERIC NOT NULL, weight_lower_range NUMERIC NOT NULL, partner_id BIGSERIAL REFERENCES logistic_partners(id))")


conn.commit()

from data.aramex import add
from data.ups_eco import add
from data.ups_ex import add
from data.shiprocket import add
from data.dtdc import add
from data.bluedart import add
from data.shiprocket import add
from data.aramex import insert_data
from data.bluedart import insert_data
from data.dtdc import insert_data
from data.shiprocket import insert_data
from data.ups_eco import insert_data
from data.ups_ex import insert_data