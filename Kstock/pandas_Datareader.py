# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 21:44:10 2018

@author: KeunBin
"""

import pandas_datareader.data as web
import matplotlib.pyplot as plt
import datetime

start = datetime.datetime(2014, 2, 19)
end = datetime.datetime(2016, 3, 4)

gs = web.DataReader("078930.KS", "yahoo", start, end)
new_gs = gs[gs['Volume'] != 0]  #거래량이 0 인 데이터 삭제

ma5 = new_gs['Adj Close'].rolling(window=5).mean() # 5일 이동 평균선
ma20 = new_gs['Adj Close'].rolling(window=20).mean() # 20일 이동 평균선
ma60 = new_gs['Adj Close'].rolling(window=60).mean() # 60일 이동 평균선
ma120 = new_gs['Adj Close'].rolling(window=120).mean() # 120일 이동 평균선

new_gs.insert(len(new_gs.columns), "MA5", ma5)
new_gs.insert(len(new_gs.columns), "MA20", ma20)
new_gs.insert(len(new_gs.columns), "MA60", ma60)
new_gs.insert(len(new_gs.columns), "MA120", ma120)

plt.plot(new_gs.index, new_gs['MA5'], label="MA5")
plt.plot(new_gs.index, new_gs['MA20'], label="MA20")
plt.plot(new_gs.index, new_gs['MA60'], label="MA60")
plt.plot(new_gs.index, new_gs['MA120'], label="MA120")
plt.plot(new_gs.index, new_gs['Adj Close'])
plt.legend(loc="best")
plt.grid()
plt.show()