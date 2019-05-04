!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" @author: JGJ """

# load images of the digits 0 through 5 
from sklearn.datasets import load_digits
digits = load_digits(n_class=6)

# Visualize few digits
fig, ax = plt.subplots(8, 8, figsize=(3, 3)) #(4,4) or (6,6) also will display
for i, axi in enumerate(ax.flat):
    axi.imshow(digits.images[i], cmap='binary')
    axi.set(xticks=[], yticks=[])

# project the digits into 2 dimensions using IsoMap
from sklearn.manifold import Isomap
iso = Isomap(n_components=2)
projection = iso.fit_transform(digits.data)

# Plot manifold embedding of handwritten digits
plt.scatter(projection[:, 0], projection[:, 1], lw=0.1, c=digits.target, cmap=plt.cm.get_cmap('cubehelix', 6))
plt.colorbar(ticks=range(6), label='digit value') # tikcs used
plt.clim(-0.5, 5.5) # clims added
