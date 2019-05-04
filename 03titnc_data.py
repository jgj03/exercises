#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Created on Mon Apr 15 14:19:13 2019
@author: JGJ"""

import numpy as np
import pandas as pd
import seaborn as sns
titan = sns.load_dataset('titanic')
titan.info()
titan.describe()
titan.head()
titan['survived'].unique()
titan.survived.unique()
titan.columns

#Check the survial rate by gender
titan.groupby('sex')[['survived']]
titan.groupby('sex')[['survived']].mean()

titan.columns
titan.class.unique()# ERROR : SyntaxError: invalid syntax
titan['class'].unique()

#check the gender and class based survival rate
titan.groupby(['sex', 'class'])['survived'].aggregate('mean')
titan.groupby(['sex', 'class'])['survived'].aggregate('mean').unstack()

#Same operation as above using pivot_table
titan.pivot_table('survived', index='sex', columns='class')
titan.pivot_table('survived', index='class', columns='sex')

#Multi level pivot
age = pd.cut(titan['age'], [0, 18, 80])
titan.pivot_table('survived',['sex', age],'class')

titan.fare.unique()
fare = pd.qcut(titan['fare'],2)
titan.pivot_table('survived', ['sex',age],[fare, 'class'])

#Additional pivot_table options
titan.pivot_table('survived', index='sex', columns='class', margins=True)
