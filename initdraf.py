from pylab import *
fpre_his,fpre_his2,thetaa,J_hisa,alphaa=[],[],[],[],[]
file0,file1,file2=files[2],files[1],files[0]
X,y=loadd.onest(file0,2,[0,6,8],6)
Xt,yt=loadd.onest(file1,2,[0,6,8],6)
Xt=mat(Xt)
Xtt,ytt=loadd.onest(file2,2,[0,6,8],6)
Xtt=mat(Xtt)
D=ones((len(y),1))/len(y)
itert=100

def supre(Xt,yt,thetaa,alphaa):
    m=len(Xt)
    p1a1,p1a0,p0a0=0,0,0
    for j in range(m):
        temp=0        
        for k in range(len(thetaa)):
            temp+=Xt[j]*thetaa[k]*alphaa[k]
        if temp>0 and yt[j]==1:
            p1a1+=1
        elif temp>0 and yt[j]==0:
            p1a0+=1
        elif temp<0 and y[j]==0:
            p0a0+=1
    right1=float(p1a1+p0a0)/m
    right2=p1a1/float(p1a1+p1a0)
    return right1,right2
    
for i in range(itert):
    theta,J_his=logi.grandient(X,y,0.5,1000,D)
    thetaa.append(theta)
    J_hisa.append(J_his)
    pre,rig,err=logi.predict(Xt,yt,thetaa[i])
    alphaa.append(log(rig/(1-rig))/2)
    for j in range(len(err)):
        if err[j]==1:
            D[j]=D[j]*exp(-alphaa[i])
        else :
            D[j]=D[j]*exp(alphaa[i])
    D=D/float(sum(D))
    fpre_his.append(supre(Xt,yt,thetaa,alphaa))
    fpre_his2.append(supre(Xtt,ytt,thetaa,alphaa))