#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 4 10:12:46 2021
@author: ashleycook
"""
import os 

os.environ["PROJ_LIB"] = "/Applications/Anaconda-Navigator.app"
import sqlite3 as sl
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import pandas as pd

FLIGHTS_DB = "/Users/ashleycook/Downloads/flights.db"

def main():
    
    connection = sl.connect(FLIGHTS_DB)
    
    query = """
    select cast(sa.longitude as float) as source_lon,
    cast(sa.latitude as float) as source_lat,
    cast(da.longitude as float) as dest_lon,
    cast(da.latitude as float) as dest_lat
    from routes
    inner join airports sa on sa.id = routes.source_id
    inner join airports da on da.id = routes.dest_id 
"""
    routes = pd.read_sql_query(query, connection)
    connection.close()
    
    myMap = Basemap(
        projection = 'merc',
        llcrnrlat = -80,
        urcrnrlat = 80, 
        llcrnrlon = -180,
        urcrnrlon = 180,
        lat_ts = 20,
        resolution = 'c')
    
    myMap.drawcoastlines()
    
    for name, row in routes[:3000].iterrows():
        if abs(row["source_lon"] - row["dest_lon"]) < 90:
            myMap.drawgreatcircle(row["source_lon"],
                                  row["source_lat"],
                                  row["dest_lon"],
                                  row["dest_lat"],
                                  linewidth = 1,
                                  color = 'b')
            
 

main()