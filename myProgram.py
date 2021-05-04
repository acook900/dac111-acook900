#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 4 10:12:46 2021
@author: ashleycook
"""

import sqlite3 as sl

FLIGHTS_DB = "/Users/ashleycook/Downloads/flights.db"

def main():
    #Holds connection between database so we can interact with database
    connection = sl.connect(FLIGHTS_DB)
    cursor = connection.cursor()
    
    query = "select * from airlines limit 5;"
    cursor.execute(query)
    
    results = cursor.fetchall()
    print(results)
    
    cursor.close()
    connection.close()
    
main()