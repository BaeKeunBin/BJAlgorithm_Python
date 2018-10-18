# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 19:01:05 2018

@author: KeunBin
"""

N = int(input())
Num = int(input())
s=0
for i in range(1,N+1):
    print(s)
    s+= int(Num/(10**(N-i)))