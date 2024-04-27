# -*- coding: utf-8 -*-
"""
Created on Thu Feb 29 16:41:28 2024

@author: localuser
"""
import numpy as np 
import scipy.stats as sps
pi=np.random.rand()
mu1,mu2=8*np.random.rand(2)
sigma1,sigma2=2*np.random.rand(2)
x=np.zeros(10000)
for i in range(10000):
    if np.random.rand()<pi:
        x[i]=np.random.normal(mu1,sigma1)
    else:
        x[i]=np.random.normal(mu2,sigma2)
        


p=0.5
m1,m2=-np.random.rand(),np.random.rand()
s1=s2=np.var(x)

m1_p,p_p,m2_p,s1_p,s2_p=0,0,0,0,0
while(abs(p_p-p)>1e-6 or abs(m1_p-m1)>1e-6 or abs(s1_p-s1)>1e-6):
    y=(p*sps.norm.pdf(x,m1,np.sqrt(s1)))/(p*sps.norm.pdf(x,m1,np.sqrt(s1))+(1-p)*sps.norm.pdf(x,m2,np.sqrt(s2))) 
    m1_p,m2_p,s1_p,s2_p,p_p=m1,m2,s1,s2,p
    m1=y.dot(x)/np.sum(y) 
    s1=y.dot((x-m1)**2)/np.sum(y)
    m2=(1-y).dot(x)/np.sum(1-y)
    s2=(1-y).dot((x-m2)**2)/np.sum(1-y)
    p=y.mean()

print("Population Parameters",pi,mu1,mu2,sigma1**2,sigma2**2)
print("Estimated Parameters",p,m1,m2,s1,s2)
