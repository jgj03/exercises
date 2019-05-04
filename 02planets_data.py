#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Created on Fri Apr 12 16:51:46 2019
@author: JGJ """

import seaborn as sns
planets = sns.load_dataset('planets') # details on the 1,000+ exoplanets discovered up to 2014.
planets.shape
planets.keys()
planets.head()
planets.info()
planets.describe()
planets.method.unique()
#dropping rows with missing values:
planets.dropna().describe()
planets.groupby('method')
planets.groupby('method')['orbital_period']
planets.groupby('method')['orbital_period'].median()
for (method, group) in planets.groupby('method'):
    print("{0:10s} shape={1}".format(method, group.shape))
s=10
print("{0:10s}".format(s))
planets.groupby('method')['year']
planets.groupby('method')['year'].describe()
planets.groupby('method')['year'].describe().unstack()

## Grouping example
decade = 10*planets['year']//10
decade
decade = decade.astype(str) + 's'
decade
decade.name = 'decade'
decade
planets.groupby(['method',decade])['number'].sum().unstack().fillna(0)




