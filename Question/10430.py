# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 17:34:49 2018

@author: KeunBin
"""

x,y,z = map(int,input().split())
print((x+y)%z)
print((x%z+y%z)%z)
print((x*y)%z)
print((x%z*y%z)%z)