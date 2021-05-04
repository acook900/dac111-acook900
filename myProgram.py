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

FLIGHTS_DB = "/Users/ashleycook/Downloads/flights.db"

def main():
    #Holds connection between database so we can interact with database
    connection = sl.connect(FLIGHTS_DB)
    cursor = connection.cursor()
    
    
    coords = cursor.execute(
"""
select cast(longitude as float), 
cast(latitude as float)
from airports;                        
"""
    ).fetchall()
    
    cursor.close()
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
    myMap.drawmapboundary()
    

    
main()