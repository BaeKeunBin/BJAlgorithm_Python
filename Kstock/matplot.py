# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 18:24:46 2018

@author: KeunBin
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas_datareader.data as web
#1
#plt.plot([1,2,3,4]) #plot 함수를 호출할 때 x 축 값을 따로 지정하지 않으면 자동으로 실숫값이 할당됩니다

#2
#x= range(0,100)
#y = [v*v for v in x]  # 리스트 내장
#plt.plot(x,y,"ro")
#
#3
#fig = plt.figure()
#ax1 = fig.add_subplot(2,1,1)
#ax2 = fig.add_subplot(2,1,2)
#
#ax1.plot(x,y)
#ax2.bar(x,y)

#3
#x = np.arange(0.0,2*np.pi,0.1)
#sin_Y = np.sin(x)
#cos_Y = np.cos(x)
#
#fig = plt.figure()
#ax1 = fig.add_subplot(2,1,1)
#ax2 = fig.add_subplot(2,1,2)
#
#ax1.plot(x,sin_Y,"r--")
#ax2.plot(x,cos_Y,"b--")
#
#ax1.set_xlabel("x")
#ax1.set_ylabel("sin(x)")
#
#ax2.set_xlabel("x")
#ax2.set_ylabel("cos(x)")

lg = web.DataReader("066570.KS","yahoo")
samsung = web.DataReader("005930.KS","yahoo")
plt.plot(lg.index,lg["Adj Close"], label = "LG Electronics")
plt.plot(samsung.index,samsung["Adj Close"], label = "samsung")

plt.legend(loc="upper left")


plt.show()