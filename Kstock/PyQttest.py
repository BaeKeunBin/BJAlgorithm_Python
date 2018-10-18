# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 16:55:30 2018

@author: KeunBin
"""

import sys
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)
label = QLabel("Hello PyQt")
label.show()
app.exec_()