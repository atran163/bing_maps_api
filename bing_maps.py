import pandas as pd
import requests
from pandas.io.json import json_normalize


# Using bing maps api, how many "Bay Wheels" Bike stations are there 
df = pd.read_csv('drive/My Drive/dataframe.csv')
ford_go_bike = df[df["networkid"] == "ford-gobike"]


import time
bikes = []
for index, row in ford_go_bike.iterrows():
    # get the episodes for the show from the REST API
    response = requests.get("http://dev.virtualearth.net/REST/v1/Locations/%f,%f?includeEntityTypes=Address&key=Aj_3HNkptijrQiHnCrZEpXjsnKR-BlfgvLNHeaWlOCP7_hT4-YUzD1GTnQBhqkAe" % (row.latitude, row.longitude))
    bikes.append(response.json())
    
    
addresses = [bike['resourceSets'][0]["resources"][0]["address"] for bike in bikes]

df_addresses = json_normalize(addresses)

df_addresses["adminDistrict2"].value_counts() 
# There are 221 bike stations in SF



