# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 16:11:26 2018

@author: KeunBin
"""
import win32com.client

word = win32com.client.Dispatch("Word.Application")
word.Visible = True