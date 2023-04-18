# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 14:37:30 2023

@author: Krista
"""
import pandas as pd
import datetime

def next_weekday(d, weekday):
    days_ahead = weekday - d.weekday()
    if days_ahead <= 0: #Counting current day
        days_ahead += 7
    return d + datetime.timedelta(days_ahead)

from datetime import date
today = date.today()

#Change the number below to the future day of the week you want
#0 = Monday, 1=Tuesday, 2=Wednesday...
DayofWeek = next_weekday(today, 1)
#Print the output
Tuesday = (DayofWeek.strftime("%m/%d/%y"))



df["column name"] = Tuesday
