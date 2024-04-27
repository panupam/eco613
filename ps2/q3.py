import numpy as np 
import scipy.stats as sps
import matplotlib.pyplot as plt

# x=sps.skewnorm.ppf(np.random.rand(100),a=1)
x=sps.skewnorm.rvs(a=1,size=1000)

B=int(input("Enter B "))
krt=np.zeros(B)
kr2=np.zeros(B)
for i in range(B):
    s=x[np.array(np.floor(x.size*np.random.rand(x.size)),dtype=int)]
    s1=x[np.array(np.floor(x.size*np.random.rand(x.size)),dtype=int)]
    krt[i]=sps.kurtosis(s)
    kr2[i]=sps.kurtosis(s1)


krt.sort()
bt=sps.bootstrap((x,),n_resamples=B,statistic=sps.kurtosis)
kr2.sort()
print("Confidence interval is", krt[int(np.floor(krt.size*0.025))],krt[int(np.ceil(krt.size*0.975))])
print("Confidence interval is", kr2[int(np.floor(krt.size*0.025))],kr2[int(np.ceil(krt.size*0.975))])

print("From bootstrap command",bt.confidence_interval)


plt.hist(krt,bins=30)
plt.hist(kr2,bins=30)
# plt.hist(bt.bootstrap_distribution,bins=30)
plt.show()
