# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 18:13:33 2018

@author: KeunBin
"""
N = input()

for i in range(1,int(N)+1):
    for j in range(0,i):
        print("*",end="")
    print("\n",end="")
