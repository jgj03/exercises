#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" @author: mechrnd """


import numpy as np
import pandas as pd

cities = pd.read_csv('california_cities.csv')
cities.head()
cities.info()

# Extract the data top plot
lat = cities['latd'].values
lon = cities['longd'].values
population = cities['population_total'].values
area = cities['area_total_km2'].values

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

# Draw the map background
fig = plt.figure(figsize=(8, 8))
m = Basemap(projection='lcc', resolution='h', lat_0=37.5, lon_0=-119, width=1E6, height=1.2E6)
m.shadedrelief()
m.drawcoastlines(color='gray')
m.drawcountries(color='gray')
m.drawstates(color='gray')

# Scatter city data, with color reflecting population and size reflecting area
m.scatter(lon, lat, latlon=True, c=np.log10(population), s=area, cmap='Reds', alpha=0.5)

# Create colorbar and legend
plt.colorbar(label=r'$\log_{10}({\rm population})$')
plt.clim(3, 7)
# make legend with dummy points
for a in [100, 300, 500]:
    plt.scatter([], [], c='k', alpha=0.5, s=a,
                label=str(a) + ' km$^2$')
    plt.legend(scatterpoints=1, frameon=False, labelspacing=1, loc='lower left');
    
    
    
    