#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" @author: JGJ """

import pandas as pd

try:
    recipes = pd.read_json('recipeitems-latest.json')
except ValueError as e:
    print("ValueError:", e)
# read the entire file into a Python array

with open('recipeitems-latest.json', 'r') as f:
    # Extract each line
    data = (line.strip() for line in f)
    # Reformat so each line is the element of a list
    data_json = "[{0}]".format(','.join(data))
# read the result as a JSON
recipes = pd.read_json(data_json)
recipes.shape
recipes.columns
recipes.info()
recipes.columns
recipes.head()
recipes.iloc[0]
# Closer look at ingredients
recipes.ingredients.str.len()
recipes.ingredients.str.len().describe()
#avg 250 characters with a minimum of 0 & max of 9067

import numpy as np
# See the longest ingredient
recipes.name[np.argmax(recipes.ingredients.str.len())] #FutureWarning: 'argmax' is deprecated. Use 'idxmax' instead.

# See the number of recipes for breakfast food
recipes.description.str.contains('[Bb]reakfast').sum()
# how many recipes for cinnamon as iongredient
recipes.ingredients.str.contains('[Cc]innamom')
recipes.ingredients.str.contains('[Cc]innamom').sum()
recipes.ingredients.str.contains('[Cc]inamom').sum()

## Creating a recipe recommender : given a list of ingredients, find a recipe that uses all those ingredients.
spice_list = ['salt', 'pepper', 'oregano', 'sage', 'parsley', 'rosemary', 'tarragon', 'thyme', 'paprika', 'cumin']

import re
spice_df = pd.DataFrame(dict((spice, recipes.ingredients.str.contains(spice, re.IGNORECASE))for spice in spice_list))
spice_df.head()

# Find a recipe that uses parsley, paprika, and tarragon
selection = spice_df.query('parsley & paprika & tarragon') 
selection
len(selection)
# use the index returned by this selection to discover the names of the recipes that have this combination.
recipes.name[selection.index]

A simple recommeneder is narrowed down with items available in hand

