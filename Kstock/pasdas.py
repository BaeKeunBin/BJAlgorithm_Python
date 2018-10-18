# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 21:34:59 2018

@author: KeunBin
"""

from pandas import Series, DataFrame

raw_data  = { 'col0' : [1,2,3,4],
             'col1' : [10,20,30,40],
             'col2' : [100,200,300,400]}

data = DataFrame(raw_data)
print(data)

data1 = data['col1']
print(data1)