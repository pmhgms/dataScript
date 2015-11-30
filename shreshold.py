import logi
import glob
import loadd
from matplotlib.pyplot import *

a=[i/10.0 for i in range(-5,20)]
files=[x for x in glob.glob('*.pickle')]

def rigmax(X,y,theta):
    b=[]
    for i in a:
        try:
            pre,rig=logi.predict(X,y,theta,i)
            b.append(rig)
        except ZeroDivisionError:
            return b
    return b
       
def howrare(theta,speCol=None,speStar=0):
    X=[] 
    ma=0   
    for onefile in files:
        x,y=loadd.onest(onefile,2,[8],6,speCol,speStar)
        X.append(x)
        ma+=len(y)
    b=[]
    for thre in a:
        p1a1=0
        for x in X:
            m=len(x)
            for i in range(m):
                if x[i]*theta>thre:
                    p1a1+=1
        b.append(p1a1/float(ma))
    plot(a[:len(b)],b)
    return b
    
def curforrig(theta,fealist,cond):
    for onefile in files:
        x,y=loadd.onest(onefile,2,fealist,6)
        if len(y)>cond:
            b=rigmax(x,y,theta)
            plot(a[:len(b)],b)