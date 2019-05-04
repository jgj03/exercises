#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" @author: JGJ """

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

from netCDF4 import Dataset
data = Dataset('gistemp250.nc')

from netCDF4 import date2index
from datetime import datetime
timeindex = date2index(datetime(2014, 1, 15),
data.variables['time'])

lat = data.variables['lat'][:]
lon = data.variables['lon'][:]
lon, lat = np.meshgrid(lon, lat)
temp_anomaly = data.variables['tempanomaly'][timeindex]

# Plot and visualize
fig = plt.figure(figsize=(10, 8))
m = Basemap(projection='lcc', resolution='c', width=8E6, height=8E6, lat_0=45, lon_0=-100,)
m.shadedrelief(scale=0.5)
m.pcolormesh(lon, lat, temp_anomaly, latlon=True, cmap='RdBu_r')
plt.clim(-8, 8)
m.drawcoastlines(color='lightgray')
plt.title('January 2014 Temperature Anomaly')
plt.colorbar(label='temperature anomaly (°C)');


