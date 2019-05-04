#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" @author: JGJ """

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('marathon-data.csv')
data.head()
data.info()
data.dtypes # time is loaded as objects,ie python strings

def convert_time(s):
    h, m, s = map(int, s.split(':'))
    return pd.datetools.timedelta(hours=h, minutes=m, seconds=s) 

data = pd.read_csv('marathon-data.csv', converters={'split':convert_time, 'final':convert_time})
data.head()
data.dtypes

# Convert time to seconds
1E9
data['split_sec'] = data['split'].astype(int)/1E9
data['final_sec'] = data['final'].astype(int)/1E9
data.head()

# Visualization
import seaborn as sns
with sns.axes_style(style='white'):
    g = sns.jointplot('split_sec', 'final_sec', data)
    g.ax_joint.plot(np.linspace(4000, 16000), np.linspace(8000, 32000), ':k')
    
fr_sec = 2 * data['split_sec']/data['final_sec']
data['split_frac'] = 1 - 2 * data['split_sec'] / data['final_sec']
data.head()

# plot split_fraction
sns.distplot(data['split_frac'])
sns.distplot(data['split_frac'], kde=False);
plt.axvline(0, color="k", linestyle="--");

sum(data.split_frac<0) # negative splits in marathon

# Correlation between split fraction and other variables.
sns.PairGrid?
g = sns.PairGrid(data, vars=['age', 'split_sec', 'final_sec', 'split_frac'], hue='gender', palette='RdBu_r')
g.map(plt.scatter, alpha=0.8)
g.add_legend();

# Difference between M & F split fractions
sns.kdeplot(data.split_frac[data.gender=='M'], label='men', shade=True)
sns.kdeplot(data.split_frac[data.gender=='W'], label='women', shade=True)
plt.xlabel('split_frac');    

# Bimodal distribution among M & F : Violinplot
sns.violinplot?
sns.violinplot('gender', 'split_frac', data=data, palette=['lightblue', 'lightpink']);

# Violin plot as a function of gender and age
data['age_dec'] = data.age.map(lambda age: 10 * (age//10))
data.head()
sns.violinplot('age_dec', 'split_frac', data=data, palette=['lightblue', 'lightpink']); # OR
sns.violinplot('age_dec', 'split_frac', hue='gender', data=data, palette=['lightblue', 'lightpink']); # OR
sns.violinplot('age_dec', 'split_frac', hue='gender', data=data, split=True, inner='quartile', 
               palette=['lightblue', 'lightpink']); # OR
#
men = (data.gender == 'M')
women = (data.gender == 'W')
with sns.axes_style(style=None):
    sns.violinplot("age_dec", "split_frac", hue="gender", data=data, split=True, inner="quartile",
                   palette=["lightblue", "lightpink"]);
# Elder aged
(data.age>80).sum()    

# regplot to fit a linear regression to the data  automatically
g = sns.lmplot('final_sec', 'split_frac', col='gender', data=data,markers=".", scatter_kws=dict(color='c'))
g.map(plt.axhline, y=0.1, color="k", ls=":");
