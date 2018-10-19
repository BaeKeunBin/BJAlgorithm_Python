# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 17:17:19 2018

@author: KeunBin
"""

import sys
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setWindowTitle("Review")

        btn1 = QPushButton("Click me", self)
        btn1.move(20, 20)
        btn1.clicked.connect(self.btn1_clicked)

    def btn1_clicked(self):
        QMessageBox.about(self, "message", "clicked")


app = QApplication(sys.argv)

mywindow = MyWindow()
mywindow.show()

app.exec_()