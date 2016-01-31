# -*- coding: utf-8 -*-
"""
Created on Sun May 24 18:28:35 2015

@author: pmhgms
"""
oriSet, listn=input('list,len:\n')
firstPartOfSubSet, total, l, firstPartLength=[],[],0,0

def digui(firstPartOfSubSet, l, firstPartLength, subSetLength):
    if firstPartLength +1 < subSetLength:
        firstPartLength += 1
        for startPosition in range(l, len(oriSet)-subSetLength+firstPartLength):
            digui(firstPartOfSubSet + [oriSet[startPosition]], startPosition+1, firstPartLength, subSetLength)
    else :
        for j in range(l, en(oriSet)):
            total.append(firstPartOfSubSet + [oriSet[j]])

def gene():            
    for subSetLength in listn:
        digui(firstPartOfSubSet, l, firstPartLength, subSetLength)
        
gene()