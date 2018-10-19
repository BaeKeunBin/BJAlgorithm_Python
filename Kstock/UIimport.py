# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 17:50:14 2018

@author: KeunBin
"""

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("test1.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


app = QApplication(sys.argv)
myWindow = MyWindow()
myWindow.show()
app.exec_()