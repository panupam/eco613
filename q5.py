import numpy as np 
import scipy.stats as sps
pi=np.random.rand()
p=np.random.rand(2)
size=10000
x=np.zeros(size)
n=20
for i in range(size):
    if np.random.rand()<pi:
        x[i]=np.random.binomial(n,p[0])
    else:
        x[i]=np.random.binomial(n,p[1])
    


pih=0.5
ph=np.random.rand(2)
pp=np.zeros(2)
pihp=0
while (abs(pihp-pih)>1e-6) or (abs(ph[0]-pp[0])>1e-6):
    pp,pihp=ph,pih 
    y=(pih*sps.binom.pmf(x,n,ph[0]))/(pih*sps.binom.pmf(x,n,ph[0])+(1-pih)*sps.binom.pmf(x,n,ph[1]))
    ph[0]=y.dot(x)/(sum(y)*20)
    ph[1]=(1-y).dot(x)/(sum(1-y)*20)
    pih=y.mean()

print("Poplation Parameter",pi,p)
print("Estimated Parameter",pih,ph)