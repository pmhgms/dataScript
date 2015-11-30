# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 15:27:08 2015

@author: pmhgms
"""
import pickle
from random import randint
from ana_temp import pickAsFunToLoop, pickAsFunToLoop2
'''
for i in range(100):
    code = pickle.load(open(r'C:\Users\pmhgms\Desktop\machine_leaning\DataSet\stock_code.pickle','rb'))
    instrument = code[randint(0, len(code))]
    pickAsFunToLoop(instrument)
    pickAsFunToLoop(instrument,1)
'''    
    
for i in range(5):
    code = pickle.load(open(r'C:\Users\pmhgms\Desktop\machine_leaning\DataSet\downloadedcode.pickle','rb'))
    instrument = code[randint(0, len(code))]
    pickAsFunToLoop2(instrument)