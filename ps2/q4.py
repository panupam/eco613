import numpy as np 
import scipy.stats as sps

x=sps.skewnorm.rvs(a=1,size=1000)

sps.monte_carlo_test(x,np.random.normal,sps.kurtosis,alternative="greater")
