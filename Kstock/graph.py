# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 19:11:28 2018

@author: KeunBin
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas_datareader.data as web

sk_hynix = web.DataReader("000660.KS","yahoo")

fig = plt.figure(figsize=(12,8))

top_axes = plt.subplot2grid((4,4),(0,0),rowspan=3,colspan=4)
bottom_axes = plt.subplot2grid((4,4),(3,0),rowspan=1,colspan=4)
bottom_axes.get_yaxis().get_major_formatter().set_scientific(False)
#거래량 값으로서 큰 값이 발생할 때 그 값을 오일러 상수(e)의 지수 형태로 표현되지 않게 해줍니다.

top_axes.plot(sk_hynix.index, sk_hynix['Adj Close'], label='Adjusted Close')
bottom_axes.plot(sk_hynix.index, sk_hynix['Volume'])

plt.tight_layout() #  subplot들이 Figure 객체의 영역 내에서 자동으로 최대 크기로 출력
plt.show()