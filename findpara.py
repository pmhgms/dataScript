import loadd
import logi

def oneee(filename,filenamet,fealist,numfu0,numfue):
    pre=[]
    for i in range(numfu0,numfue):
        X,y=loadd.onest(filename,i,fealist,6)
        Xt,yt=loadd.onest(filenamet,i,fealist,6)
        theta,J_his=logi.grandient(X,y,0.5,1000)
        try:
            pren,rig=logi.predict(X,y,theta)
            pre.append(pren)
        except ZeroDivisionError:
            break
    print pre.index(max(pre)),max(pre)
    return pre