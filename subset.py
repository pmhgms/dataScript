# -*- coding: utf-8 -*-
"""
Created on Sun May 24 18:28:35 2015

@author: pmhgms
"""
m,listn=input('list,len:\n')
head,total,l,k=[],[],0,0

def digui(head,l,k,n):
    if k+1<n:
        k+=1
        for i in range(l,len(m)-n+k):
            digui(head+[m[i]],i+1,k,n)
    else :
        for j in range(l,len(m)):
            total.append(head+[m[j]])

def gene():            
    for n in listn:
        digui(head,l,k,n)
        
gene()