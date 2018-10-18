# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 18:01:01 2018

@author: KeunBin
"""

N = input()

for i in range(1,10):
    temp = str(N)+" * "+str(i)+" = "+str(int(N)*i)
    print(temp)