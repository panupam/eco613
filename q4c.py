import numpy as np 
import scipy.stats as sps
p=np.array([0.2, 0.3,0.5])
size=10000
mu=8*np.random.rand(3)
sigma=2*np.random.rand(3)
x=np.zeros(size)
for i in range(size):
    u=np.random.rand()
    if u<p[0]:
        x[i]=np.random.normal(mu[0],sigma[0])
    elif u<sum(p[:-1]):
        x[i]=np.random.normal(mu[1],sigma[1])
    else:
        x[i]=np.random.normal(mu[2],sigma[2])


pi=np.array([1/3,1/3,1/3])
m=np.random.rand(3)*2 
s=np.array([x.var()]*3)
mp=sp=pip=np.zeros(3)

while (abs(pi[0]-pip[0])>1e-6) or (abs(m[0]-mp[0])>1e-6) or (abs(s[0]-sp[0])>1e-6):
    mp,sp,pip=m,s,pi
    y1=(pi[0]*sps.norm.pdf(x,m[0],np.sqrt(s[0])))/(pi[0]*sps.norm.pdf(x,m[0],np.sqrt(s[0]))+pi[1]*sps.norm.pdf(x,m[1],np.sqrt(s[1]))+pi[2]*sps.norm.pdf(x,m[2],np.sqrt(s[2])))
    y2=(pi[1]*sps.norm.pdf(x,m[1],np.sqrt(s[1])))/(pi[0]*sps.norm.pdf(x,m[0],np.sqrt(s[0]))+pi[1]*sps.norm.pdf(x,m[1],np.sqrt(s[1]))+pi[2]*sps.norm.pdf(x,m[2],np.sqrt(s[2])))
    y3=(pi[2]*sps.norm.pdf(x,m[2],np.sqrt(s[2])))/(pi[0]*sps.norm.pdf(x,m[0],np.sqrt(s[0]))+pi[1]*sps.norm.pdf(x,m[1],np.sqrt(s[1]))+pi[2]*sps.norm.pdf(x,m[2],np.sqrt(s[2])))
    m[0]=y1.dot(x)/sum(y1)
    s[0]=y1.dot((x-m[0])**2)/sum(y1)
    m[1]=y2.dot(x)/sum(y2)
    s[1]=y2.dot((x-m[1])**2)/sum(y2)
    m[2]=y3.dot(x)/sum(y3)
    s[2]=y3.dot((x-m[2])**2)/sum(y3)
    pi[0]=y1.mean()
    pi[1]=y2.mean()
    pi[2]=y3.mean()

print("Initial is",p,mu,sigma**2)
print("Estimated is",pi,m,s)

