#!/usr/bin/env python
# coding: utf-8

# In[37]:


import numpy as np
import pandas as pd
from datetime import datetime as dt
from googlemaps import GoogleMaps


# In[41]:


df = pd.read_csv("https://www.gstatic.com/covid19/mobility/Global_Mobility_Report.csv?cachebust=6d352e35dcffafce")
df = df.fillna(method='ffill')
df = df.replace(np.nan, '', regex=True)
df


# In[ ]:


def get_geo_coordinates(address):
    gmaps = GoogleMaps(api_key)
    lat,lng = gmaps.address_to_latlng(address)
    return (lat, lng)


# In[48]:


#Get all data
df = pd.read_csv("https://www.gstatic.com/covid19/mobility/Global_Mobility_Report.csv?cachebust=6d352e35dcffafce")
df = df.fillna(method='ffill')
df = df.replace(np.nan, '', regex=True)
place_data = {}
print((dt.strptime(df.iloc[2]["date"],'%Y-%m-%d')-dt.strptime(df.iloc[0]["date"],'%Y-%m-%d')).total_seconds())
for i in range(len(df)-1):
    row_one = df.iloc[i]
    date_one = dt.strptime(df.iloc[i]["date"], '%Y-%m-%d')
    date_two = dt.strptime(df.iloc[i+1]["date"], '%Y-%m-%d')
    seconds_difference = (date_two - date_one).total_seconds()
    if seconds_difference < 0:
        address = df.iloc[i]["country_region"] + " "
        address += df.iloc[i]["sub_region_1"] + " "
        address += df.iloc[i]["sub_region_2"] + " "
        print(address)
        place_data[address] = row_one["retail_and_recreation_percent_change_from_baseline"] + row_one["grocery_and_pharmacy_percent_change_from_baseline"] + row_one["parks_percent_change_from_baseline"] + row_one["transit_stations_percent_change_from_baseline"] + row_one["workplaces_percent_change_from_baseline"] + row_one["residential_percent_change_from_baseline"]
print(place_data)


# In[ ]:


#Get New York data
df = pd.read_csv("https://www.gstatic.com/covid19/mobility/Global_Mobility_Report.csv?cachebust=6d352e35dcffafce")
df = df.fillna(method='ffill')
df = df.replace(np.nan, '', regex=True)
place_data = {}
print((dt.strptime(df.iloc[2]["date"],'%Y-%m-%d')-dt.strptime(df.iloc[0]["date"],'%Y-%m-%d')).total_seconds())
for i in range(len(df)-1):
    row_one = df.iloc[i]
    if (df.iloc[i]["sub_region_1"] == "New York"):
        date_one = dt.strptime(df.iloc[i]["date"], '%Y-%m-%d')
        date_two = dt.strptime(df.iloc[i+1]["date"], '%Y-%m-%d')
        seconds_difference = (date_two - date_one).total_seconds()
        if seconds_difference < 0:
            address = df.iloc[i]["country_region"] + " "
            address += df.iloc[i]["sub_region_1"] + " "
            address += df.iloc[i]["sub_region_2"] + " "
            print(address)
            place_data[address] = row_one["retail_and_recreation_percent_change_from_baseline"] + row_one["grocery_and_pharmacy_percent_change_from_baseline"] + row_one["parks_percent_change_from_baseline"] + row_one["transit_stations_percent_change_from_baseline"] + row_one["workplaces_percent_change_from_baseline"] + row_one["residential_percent_change_from_baseline"]
print(place_data)


# In[ ]:




