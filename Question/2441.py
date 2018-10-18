# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 18:34:48 2018

@author: KeunBin
"""

N = input()
fm = "{0:>"+N+"}"
for i in range(1,int(N)+1):
    temp=""
    i = int(N)+1-i
    for j in range(0,i):
        temp+="*"
    print(fm.format(temp),end="")    
    print("\n",end="")
