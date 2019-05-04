#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" @author: JGJ """

from pandas_datareader import data
goog = data.DataReader('GOOG', start='2004', end='2016', data_source='google') 
#Shows error in pandas 0.7.0 & higher update:ImmediateDeprecationError: 
pd.__version__
goog.head()

# Using the close price alone
goog = goog['Close']

# Visualization
%matplotlib inline
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
goog.plot()

# Resampling and converting frequencies in time series analysis
# Googles's closing price plot
goog.plot(alpha=0.5, style='-')
goog.resample('BA').mean().plot(style=':') # data aggregation
goog.asfreq('BA').plot(style='--'); # data selection
plt.legend(['input', 'resample', 'asfreq'], loc='upper left');

# Resamplings of Google’s stock price
goog.plot(alpha=0.5, style='-')
goog.resample('BA').mean().plot(style=':')
goog.asfreq('BA').plot(style='--');
plt.legend(['input', 'resample', 'asfreq'], loc='upper left');

# Resampling business day data at a daily frequency
fig, ax = plt.subplots(2, sharex=True)
data = goog.iloc[:10]
data.asfreq('D').plot(ax=ax[0], marker='o')
data.asfreq('D', method='bfill').plot(ax=ax[1], style='-o')
data.asfreq('D', method='ffill').plot(ax=ax[1], style='--o')
ax[1].legend(["back-fill", "forward-fill"]);

# Time shifts
fig, ax = plt.subplots(3, sharey=True)
# apply a frequency to the data
goog = goog.asfreq('D', method='pad')
goog.plot(ax=ax[0])
goog.shift(900).plot(ax=ax[1])
goog.tshift(900).plot(ax=ax[2])
# legends and annotations
local_max = pd.to_datetime('2007-11-05')
offset = pd.Timedelta(900, 'D')
ax[0].legend(['input'], loc=2)
ax[0].get_xticklabels()[4].set(weight='heavy', color='red')
ax[0].axvline(local_max, alpha=0.3, color='red')
ax[1].legend(['shift(900)'], loc=2)
ax[1].get_xticklabels()[4].set(weight='heavy', color='red')
ax[1].axvline(local_max + offset, alpha=0.3, color='red')
ax[2].legend(['tshift(900)'], loc=2)
ax[2].get_xticklabels()[1].set(weight='heavy', color='red')
ax[2].axvline(local_max + offset, alpha=0.3, color='red');

# ROI plot
ROI = 100 * (goog.tshift(-365) / goog - 1)
ROI.plot()
plt.ylabel('% Return on Investment');

#Rolling windows : one-year centered rolling mean and standard deviation
rolling = goog.rolling(365, center=True)
data = pd.DataFrame({'input': goog, 'one-year rolling_mean': rolling.mean(),
                     'one-year rolling_std': rolling.std()})
ax = data.plot(style=['-', '--', ':'])
ax.lines[0].set_alpha(0.3)
#As with groupby operations, the aggregate() and apply() methods can be used for custom rolling computations.

