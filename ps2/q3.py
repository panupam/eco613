import numpy as np 
import scipy.stats as sps
import matplotlib.pyplot as plt

# x=sps.skewnorm.ppf(np.random.rand(100),a=1)
x=sps.skewnorm.rvs(a=1,size=100)

B=int(input("Enter B "))
krt=np.zeros(B)
for i in range(B):
    s=x[np.array(np.floor(x.size*np.random.rand(x.size)),dtype=int)]
    krt[i]=sps.kurtosis(s)

plt.hist(krt)
plt.show()
krt.sort()
bt=sps.bootstrap((x,),n_resamples=B,statistic=sps.kurtosis)
# plt.hist(bt.bootstrap_distribution)
print("Confidence interval is", krt[int(np.floor(krt.size*0.025))],krt[int(np.ceil(krt.size*0.975))])
print("From bootstrap command",bt.confidence_interval)

