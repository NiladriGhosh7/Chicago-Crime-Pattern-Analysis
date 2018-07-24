# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 11:06:15 2018

@author: Niladri
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime

crimes=pd.read_csv('Crimes_2017.csv')
str(crimes)
crimes.dtypes
crimes=crimes.dropna(axis=0)

crimes['Primary Type'] = crimes['Primary Type'].astype("category", ordered=False)
crimes['Date'] = pd.to_datetime(crimes['Date'].str[0:10],format= '%m/%d/%Y')


# 1. What are the top 12 most common crimes of the period?

Crime_By_Type=crimes[['Primary Type','Block']].groupby('Primary Type').agg('count')
Crime_By_Type.reset_index(inplace = True)
Crime_By_Type.columns=['CrimeType','Quantity']
Top_12_Crimes=Crime_By_Type.sort_values(by= 'Quantity',ascending = False)[0:12]
sns.countplot(x="Primary Type",data=crimes,palette='PuBu')
plt.show()


# 2. What are the crime types that have median above 50 crimes/day?

Crime_By_Day=crimes[['Primary Type', 'Date', 'Block']].groupby(['Primary Type','Date']).agg('count')