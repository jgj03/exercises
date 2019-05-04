#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" @author: JGJ """

import pandas as pd

births = pd.read_csv('births.csv')
births = pd.read_csv('/home/mechrnd/MV_Feature_inspection/Software/gt/Books/data/births.csv')
births.head()
births.info()
births.describe()

10*(1997/10)
# Decade-wise birth rate for M/F
births['decade']= 10 * (births['year']//10)
births.head()
births.info()
births.pivot_table('births', index='decade', columns='gender')
births.pivot_table('births', index='decade', columns='gender', aggfunc='sum') #male birth outnumbered female.

# Visualization
%matplotlib inline
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
births.pivot_table('births', index='year', columns='gender', aggfunc='sum').plot()  
plt.ylabel('Total births per year')

# Cleaning data & removing outliers
quartiles = np.percentile(births['births'], [25, 50, 75])
mu = quartiles[1]
sig = 0.74 * (quartiles[2] - quartiles[0])  #final line is a robust estimate of the sample mean, where the 0.74 comes from the interquartile range of a Gaussian distribution.
# Filter out rows with births outside these values
births = births.query('(births > @mu - 5 * @sig) & (births < @mu + 5 * @sig)')
births.info() 
# day column is float. convert it as asn integer
births['day'] = births['day'].astype(int)
births.info()

# Combine the day, month, and year to create a Date index
births.index
births.index = pd.to_datetime(10000 * births.year + 100* births.month + births.day, format='%Y%m%d')
births['dayofweek'] = births.index.dayofweek
births.head()
births.info()

# Plot births by weekday for several decades
births.pivot_table('births', index='dayofweek', columns='decade', aggfunc='mean').plot()
plt.gca().set_xticklabels(['Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun'])
plt.ylabel('mean births by day');

# Plot the mean number of births by the day of the year.
#Group the data by month and day separately
births_by_date = births.pivot_table('births', [births.index.month, births.index.day])
births_by_date.head()
births_by_date.index = [pd.datetime(2012, month, day) for (month, day) in births_by_date.index]
births_by_date.head()
# Plot the results
fig, ax = plt.subplots(figsize=(12, 4))
births_by_date.plot(ax=ax);