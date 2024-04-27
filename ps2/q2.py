import scipy.stats as sps
import numpy as np
from math import comb as c
# i=lambda n: n*i(n-1) if n>=1 else 1 #factorial
# c=lambda a, b: i(a)/(i(b)*i(a-b)) #aCb
p_cont=lambda a:c(np.sum(a[0]),a[0,0])*c(np.sum(a[1]),a[1,1])/c(np.sum(a),np.sum(a[:,0])) # probability of contingency table 
a=input("Enter matrix").split()
a=np.array([int(i) for i in a]).reshape((2,2))

b=a 
sum=0
while (b>=0).all():
    # print(1,"\n",b)
    sum+=p_cont(b)
    b=b+np.eye(2,dtype= int)
    b=b-np.array((~np.eye(2, dtype=bool)),dtype=int)   

sps.fisher_exact(a,alternative='greater') ,sum