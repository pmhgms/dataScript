from numpy import *
import pickle

def nor(data):
    data=list(data)
    mea=mean(data)
    st=std(data)
    for i in range(len(data)):
        data[i]=(data[i]-mea)/st
    return data
    
def Xy(d1,fealist,yfea,numfu,speCol,speStar,x2=None):
    X,y=[],[]
    for i in range(speStar,len(d1[yfea])-numfu-1):
        y.append(int(d1[yfea][i+numfu]>0))
        temp=[]
        for j in fealist:
            temp.extend(d1[j][i:i+numfu])
        if speCol!=None:
            temp.extend([mean(d1[speCol][i-speStar:i+numfu])])
            temp.extend([std(d1[speCol][i-speStar:i+numfu])])
        temp.extend(x2[i])
        X.append(temp)
    return X,y
    
def onest(filename,numfu,fealist,yfea,speCol=None,speStar=0):
    d1=pickle.load(open(filename,'rb'))
    x2=te(d1,numfu,yfea)
    yfea not in fealist
    for i in fealist:
        d1[i]=nor(d1[i])
    return Xy(d1,fealist,yfea,numfu,speCol,speStar,x2)

def te(d1,numfu,yfea):    
    x2=[]
    for i in range(len(d1[yfea])-numfu-1):
        t=[]
        t.append(std([d1[0][i],d1[1][i],d1[2][i],d1[3][i]]))
        t.append(std([d1[0][i+1],d1[1][i+1],d1[2][i+1],d1[3][i+1]]))
        x2.append(t)
    return x2
