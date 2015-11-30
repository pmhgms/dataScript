# -*- coding: utf-8 -*-
"""
Created on Wed May 27 19:41:55 2015

@author: pmhgms
"""

from pylab import *
from collections import Counter
file0,file1=files[5],files[3]
X0,y0=loadd.onest(file0,2,[0,6,8],6)
X1,y1=loadd.onest(file1,2,[0,6,8],6)
X0,X1=mat(X0),mat(X1)

def pre(X1,y1,X0,y0,k):
    m=len(y1)
    p1a1,p1a0,p0a0,p0a1=0,0,0,0
    for i in range(m):
        result=classify0(X1[i],X0,y0,k)
        if result==1 and y1[i]==1:
            p1a1+=1
        elif result==1 and y1[i]==0:
            p1a0+=1
        elif result==0 and y1[i]==0:
            p0a0+=1
        elif result==0 and y1[i]==1:
            p0a1+=1
    right1=float(p1a1+p0a0)/m
    right2=p1a1/float(p1a1+p1a0)
    return right1,right2
        
        
def classify0(inX, dataSet, labels, k):
    distances=array(map(lambda x:sqrt(sum(square(inX-x))) , dataSet))
    sortedDistIndicies = distances.argsort()[:k]
    return Counter(array(labels)[sortedDistIndicies]).most_common(1)[0][0]

train=[]
for k in range(2,50):    
    train.append([pre(X1,y1,X0,y0,k)]+[k])