# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 18:31:02 2018

@author: KeunBin
"""

N = input()
for i in range(1,int(N)+1):
    temp=""
    i = int(N)-i+1
    for j in range(0,i):
        temp+="*"
    print(temp,end="")    
    print("\n",end="")
