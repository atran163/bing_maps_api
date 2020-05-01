import json
import pandas as pd
from pandas.io.json import json_normalize

import requests
response = requests.get("http://api.citybik.es/v2/networks")

data = json.loads(response.text)
df = json_normalize(data, "networks")

# find all cities with bike share programs in US 
q1 = df[df["location.country"] == "US"]
q1["location.city"].nunique()


# create a df containg data about all bike stations in all networks in us 
url = "http://api.citybik.es/v2/networks/network_id"
response = requests.get(url)
import time

us = []
for city_id in q1["id"]:
    
    response = requests.get("http://api.citybik.es/v2/networks/%s" % city_id)
    us.append(response.json())
    
    time.sleep(0.5)

df_2 = json_normalize([item['network'] for item in us], 'stations', meta='id', meta_prefix='network', errors="ignore")


# find nearest bike station to coit tower

lats = df_2.latitude
longs = df_2.longitude

total1 = ((lats - 37.803).abs())
total2 = ((longs - -122.405).abs())
total = total1+total2

total.idxmin()

df_2.iloc[4823]

