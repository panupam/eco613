# -*- coding: utf-8 -*-
"""
Created on Thu Feb 29 16:15:50 2024

@author: localuser
"""
import numpy as np
n=int(input("Enter n "))
p=float(input("Enter p"))
r=int(input("enter r"))
lem=float(input("eneter lambda"))
a=[] 
b=[]
c=[]
d=[]

for i in range(10000):
    x=np.random.rand(n)
    a.append(np.sum(x<p)) # Binomial Distribution
    

for i in range(10000):
    count=1
    while np.random.rand()>p:  #Geometric
        count+=1
    
    b.append(count)

for i in range(10000):
    count=1
    cnt=0
    while cnt<r: 
        if(np.random.rand()<p):
            cnt+=1
        
        count+=1
    c.append(count) # negative binomial 
    

for i in range(10000):
    count=0
    s=0
    while (s+np.random.exponential(1/lem,1))<1:
        count+=1
    d.append(count)  # Poisson  
a=np.array(a)
b=np.array(b)
c=np.array(c)
d=np.array(d)


