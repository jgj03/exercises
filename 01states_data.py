#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" @author: JGJ """

import pandas as pd
population = pd.read_csv('/home............./state-population.csv')
area = pd.read_csv('/home/............state-areas.csv')
abbreviation = pd.read_csv('/home/.........../state-abbrevs.csv')
print(population.head()), print(area.head()), print(abbreviation.head())
print(population.shape, area.shape, abbreviation.shape)
print(population.dtypes,'\n', area.dtypes,'\n', abbreviation.dtypes)
print(population.isnull(), area.isnull(), abbreviation.isnull())
print(population.isnull().sum(),'\n', area.isnull().sum(),'\n', abbreviation.isnull().sum())
print(population.describe, '\n', area.describe,'\n', abbreviation.describe)
print(population.describe(), '\n', area.describe(),'\n', abbreviation.describe())
print(population.info, '\n', area.info,'\n', abbreviation.info)
print(population.info(), '\n', area.info(),'\n', abbreviation.info())

population.columns, area.columns, abbreviation.columns, 
#rank US states and territories by their 2010 population density.
merged = pd.merge(population, abbreviation, left_on='state/region', right_on='abbreviation', how='outer' )
merged.info()
merged.head()
#Drop duplicate information: merged.drop('abbreviation', 1) #OR
merged = merged.drop('abbreviation', axis=1)
merged.info()
merged.isnull().sum()
merged.head()
merged.isnull().any() # gives boolean output if null is present:TRUE and if no null FALSE
#figure out the null valued elements
merged[merged['population'].isnull()] #OR merged[merged['population'].isnull()].head
merged[merged['population'].isnull()].head()
merged.loc[merged['state/region'].isnull()]  
merged.loc[merged['state'].isnull(), 'state/region'].unique()
#population data includes entries for Puerto Rico (PR) and the United States as a whole (USA), while these entries do not appear in the state abbreviation key.
merged.loc[merged['state/region'] == 'PR', 'state'] = 'Puerto Rica'
merged.loc[merged['state/region'] == 'USA', 'state'] = 'United States of America' 
merged.isnull().any()
#MErge areas and merged file
merged.columns, area.columns
final = pd.merge(merged, area, on='state', how ='left')
final.columns
final.head()
final.isnull().any()
final['state'][final['area (sq. mi)'].isnull()]
final['state'][final['area (sq. mi)'].isnull()].unique()
#areas does not contain area of USA. Can insert appropriate value by summing summing all state areas. Now, just droppping null values as population density of entire US  is not relevant for this task.
final.dropna(inplace=True)
final.isnull().any()
final.info()
# Task: take data corresponding to the year 2010.
data2010 = final.query("year == 2010 & ages =='total'")
data2010.head()
data2010.columns, data2010.info()
#Compute population density and display in order. Reindex the data dn compute the results.
data2010.set_index('state', inplace=True)
density = data2010['population'] / data2010['area (sq. mi)']
density.sort_values(ascending=False) #OR
density.sort_values(ascending=False, inplace=True)
density.head()
density.tail()



