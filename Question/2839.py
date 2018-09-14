# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 17:42:18 2018

@author: KeunBin
"""

N = int(input())
s5=0
s3=0
temp=0
if N%5==0:
    s5 = int(N/5)
    print(s5)
else:
    s5= int(N/5)
    temp = N%5
    if temp%3==0:
        s3 = int(temp/3)
        print(s5+s3)
    else:
        print(-1)
