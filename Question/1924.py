# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 18:36:26 2018

@author: KeunBin
"""

month =[31,28,31,30,31,30,31,31,30,31,30,31]
day=["MON","TUE","WED","THU","FRI","SAT","SUN"]

x,y = map(int,input().split())
th=y
for i in range(0,x-1):
    th+=month[i]
    
print(day[(th%7)-1])