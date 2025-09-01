import numpy as np 
from math import comb
c=np.vectorize(comb)
e=np.random.uniform(1-np.sqrt(3),1+np.sqrt(3),10000)
a=((-0.5)**np.arange(1,7)) *c([6]*6,np.arange(1,7))
# a=a[::-1]
a
y=np.zeros(10000)
y[0]=e[0]
for i in range(1,6):
    y[i]=e[i]+np.sum(y[i-1::-1]*a[:i])

for i in range(7,10000):
    y[i]=e[i]+np.sum(y[i-1:i-7:-1]*a)



cov=lambda x,y: np.mean(x.dot(y))-np.mean(x)*np.mean(y)
Y=np.zeros(9)
Y[0]=np.var(y)
for i in range(1,9):
    Y[i]=cov(y[:-i],y[i:])

print(Y)


import numpy as np 
from math import comb
c=np.vectorize(comb)
e=np.random.normal(1,1,10000)
a=((-0.5)**np.arange(1,7)) *c([6]*6,np.arange(1,7))
a=a[::-1]

y=np.zeros(10000)
y[0]=e[0]
for i in range(1,7):
    y[i]=e[i]+np.sum(y[i-1::-1]*a[:i])

for i in range(7,10000):
    y[i]=e[i]+np.sum(y[i-1:i-7:-1]*a)



cov=lambda x,y: np.mean(x.dot(y))-np.mean(x)*np.mean(y)
Y=np.zeros(9)
Y[0]=np.var(y)
for i in range(1,9):
    Y[i]=cov(y[:-i],y[i:])

print(Y)



import numpy as np

a=np.array([-6*0.5,-15*0.25,-20*0.125,-15/2**4,-6/2**5,-1/2**6])
y=np.zeros(10000)
y[0]=np.random.uniform(1-np.sqrt(3),1+np.sqrt(3))
for i in range(1,6):
    y[i]=a[i-1::-1].dot(y[0:i])+np.random.uniform(1-np.sqrt(3),1+np.sqrt(3))
for i in range(6,10000):
    y[i]=a[5::-1].dot(y[i-6:i])+np.random.uniform(1-np.sqrt(3),1+np.sqrt(3))