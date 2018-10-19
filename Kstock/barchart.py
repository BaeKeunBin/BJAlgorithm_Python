# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 16:52:14 2018

@author: KeunBin
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager, rc
from matplotlib import style

style.use('ggplot')

font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

industry = ['통신업', '의료정밀', '운수창고업', '의약품', '음식료품', '전기가스업', '서비스업', '전기전자', '종이목재', '증권']
fluctuations = [1.83, 1.30, 1.30, 1.26, 1.06, 0.93, 0.77, 0.68, 0.65, 0.61]

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111)

#ypos = np.arange(10)
#rects = plt.barh(ypos, fluctuations, align='center', height=0.5)
#plt.yticks(ypos, industry)

#for i, rect in enumerate(rects):
#    ax.text(0.95 * rect.get_width(), rect.get_y() + rect.get_height() / 2.0, str(fluctuations[i]) + '%', ha='right', va='center')

pos = np.arange(10)
rects = plt.bar(pos, fluctuations, align='center', width=0.5)
plt.xticks(pos, industry)

for i, rect in enumerate(rects):
    ax.text(rect.get_x() + rect.get_width() / 2.0, 0.95 * rect.get_height(), str(fluctuations[i]) + '%', ha='center')
    
plt.xlabel('등락률')
plt.show()