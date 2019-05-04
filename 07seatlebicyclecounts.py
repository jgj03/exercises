#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" @author: JGJ """

import pandas as pd

#path ='/home/....../FremontBridge.csv' 
#data = pd.read_csv(path,index_col='Date', parse_dates=True)

data = pd.read_csv('FremontBridge.csv', index_col='Date', parse_dates=True)
data.head()
data.columns
data.columns = ['East', 'West']
data.columns
data['Total'] = data.eval('West + East')
data.head()
data.describe() # Summary statistics
data.info()
data.dropna().describe() # if any nan. drop it
data.info()

# Visualization
%matplotlib inline
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
data.plot()
plt.ylabel('Hourly Bicycle Count') # nothing infered from the plot

# Sample by week
weekly = data.resample('W').sum()
#weekly.plot(style=[':', '--','-'])
weekly.plot(style=['r', 'g','b'])
plt.ylabel('Weekly bicycle count');

# rolling mean also helpful for better visualization
daily = data.resample('D').sum()
daily.rolling(30, center=True).sum().plot(style=[':', '--', '-'])
plt.ylabel('mean hourly count'); #rolling mean of weekly bicylce count

# Gaussain smoothed bicycle count
daily.rolling(50, center=True, win_type='gaussian').sum(std=10).plot(style=[':', '--', '-']);

# More analysis
import numpy as np
by_time = data.groupby(data.index.time).mean()
hourly_ticks = 4 * 60 * 60 * np.arange(6)
by_time.plot(xticks=hourly_ticks, style=[':', '--', '-']); #hourly traffic

# In a  day of week
weekday = data.groupby(data.index.dayofweek).mean()
weekday.index = ['Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun']
weekday.plot(style=[':', '--', '-']);

# weekend
weekend = np.where(data.index.weekday < 5, 'Weekday', 'Weekend')
by_time = data.groupby([weekend, data.index.time]).mean()    

# Mutiple plots for visualization
import matplotlib.pyplot as plt
fig, ax = plt.subplots(1, 2, figsize=(14, 5))
by_time.ix['Weekday'].plot(ax=ax[0], title='Weekdays',
xticks=hourly_ticks, style=[':', '--', '-'])
by_time.ix['Weekend'].plot(ax=ax[1], title='Weekends',
xticks=hourly_ticks, style=[':', '--', '-']);

# More explorations
https://jakevdp.github.io/blog/2014/06/10/is-seattle-really-seeing-an-uptick-in-cycling/          