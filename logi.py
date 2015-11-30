from numpy import *
def sigmoid(z):
    return 1.0/(1+exp(-z))
    
def CostFun(X,y,theta,D=1):
    m=len(y)
    if type(D)==int:
        D=ones(shape(y))
    J=(multiply(-y,D).T*log(sigmoid(X*theta))-multiply((1-y),D).T*log(1-sigmoid(X*theta)))/m
    grad=X.T*multiply((sigmoid(X*theta)-y),D)/m
    return float(J),grad

def grandient(X,y,alpha,maxiter,D=1):
    X,y=mat(X),mat(y).T
    n=shape(X)[1]
    theta=zeros((n,1))
    J_history=[]
    for i in range(maxiter):
        J,grad=CostFun(X,y,theta,D)
        theta=theta-alpha*grad
        J_history.append(J)
    return theta,J_history
        
def predict(X,y,theta,thre=0,D=1):
    X=mat(X)
    m=len(y)
    err=ones((m,1))
    p1a1,p1a0,p0a0,p0a1=0,0,0,0
    for i in range(m):
        if X[i]*theta>thre and y[i]==1:
            p1a1+=1
        elif X[i]*theta>thre and y[i]==0:
            p1a0+=1
            err[i]=-1
        elif X[i]*theta<0 and y[i]==0:
            p0a0+=1
        elif X[i]*theta<0 and y[i]==1:
            p0a1+=1
            err[i]=-1
    right1=float(p1a1+p0a0)/m
    right2=p1a1/float(p1a1+p1a0)
    return right1,right2,err