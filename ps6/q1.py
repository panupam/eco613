import numpy as np 

# help(np.random.normal)
e=np.random.normal(0.5,np.sqrt(2),1000000)
q=int(input("Enter q: "))
a=input("Enter q space separated value: ").split()
aq=np.array([float(i) for i in a])

y=np.zeros(1000000)
for i in range(q):
    y[i]=sum(aq[:i]*e[:i])+e[i]

for i in range(q,1000000):
    y[i]=sum(aq[-1::-1]*e[i-q:i])+e[i]

#Theoretical Mean
np.mean(y)
np.sum(aq*np.array([0.5]*q))+0.5

#Variance 
np.var(y)
np.sum(aq*aq*np.array([2]*5))+2

# Cov 
cov=np.zeros(q+2)
for i in range(q+2):
    cov[i]=np.mean(y[i+1:]*y[:-i-1])-np.mean(y[i+1:])*np.mean(y[:-i-1])

cov

# import matplotlib.pyplot as plt
# plt.plot(y)

# plt.show()