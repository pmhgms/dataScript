# -*- coding: utf-8 -*-
"""
Created on Wed May 27 15:11:22 2015

@author: pmhgms
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import logi
import shreshold
from pylab import *
import glob
import loadd
files=[x for x in glob.glob('*.pickle')]
'''
file0=files.pop()
X0,y0=loadd.onest(file0,2,subset,6)
theta0,J_his=logi.grandient(X0,y0,0.5,1000)

for i in range(len(x)):
    plot(x[i])
    savefig(str(i)+'.png')
    close()
    
for subset in sst0:
    X0,y0=loadd.onest(file0,2,subset,6)
    theta0,J_his=logi.grandient(X0,y0,0.5,1000)
    shreshold.curforrig(theta0,subset,500)
    savefig(str(subset)+'.png')
    close()
    
X01,y01=[],[]
filest=files[:8]
filesv=files[-4:]

xv,yv=[],[]
for onefile  in filesv:
    X0,y0=loadd.onest(onefile,2,[8],6)
    for i in range(len(y0)):
        if X0[i]*theta>=0.6:
            xv.append(X0[i])
            yv.append(y0[i])
    '''        
import pickle
def balan():            
    while(sum(y7)+sum(mat(y7)-1)<0): 
        i=randint(0,len(y7)-1)
        if y7[i]==0:
            del x7[i]
            del y7[i]
theta0=matrix([[-0.49584613],
        [ 0.77131137]])
numfu,yfea,xshreshs=2,6,[x/10.0 for x in range(0,10)]
x7,y7=[],[]      
for totala2 in totala:
    for fealist in totala2:
        if 8 not in fealist:
            continue
        else :
            inde=fealist.index(8)
        for xshresh in xshreshs:
            x72=[]
            for onefile in files:      
                d1=pickle.load(open(onefile,'rb'))       
                for i in range(len(d1[yfea])-numfu-1):
                    temp=[]
                    t=[]
                    for j in fealist:
                        temp.extend(d1[j][i:i+numfu])
                    y7.append(int(d1[yfea][i+numfu]>0))
                    x7.append(temp)
                    t.append(std([d1[0][i],d1[1][i],d1[2][i],d1[3][i]]))
                    t.append(std([d1[0][i+1],d1[1][i+1],d1[2][i+1],d1[3][i+1]]))
                    x72.append(t)
            tx=zip(*(x7))
            tx2=[]
            for x in tx:
                tx2.append(loadd.nor(x))
            tx2.extend(zip(*(x72)))
            x7=zip(*(tx2))
            i=0
            while(i+1<len(y7)):
                if mat(x7[i][inde*2:inde*2+2])*theta0<xshresh:
                    del x7[i]
                    del y7[i]
                else :i+=1
            balan()
            theta7,J_his=logi.grandient(x7,y7,0.5,1000)
            shreshold.curforrig(theta7,fealist,500)
            text(-0.3,0.5,str(theta7))
            savefig(str(fealist)+str(xshresh)+'.png')
            close()
            x7,y7=[],[]


'''  
thrta of [0,6,7,8,9]  
[[-0.28850397]
 [ 0.37467656]
 [-0.166401  ]
 [ 0.17950507]
 [ 0.4338735 ]
 [ 0.39602966]
 [ 0.00785221]
 [ 0.37863711]
 [-0.28520223]
 [-0.37722214]]
 '''
 