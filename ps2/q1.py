import numpy as np 
import scipy.stats as st

n=int(input("Enter n ")) 
k=int(input("Enter k "))
p=float(input("Enter p "))
if k > n*p:
    print(1-st.binom.cdf(k-1,n,p),st.binomtest(k,n,p,alternative='greater'))
else:
    print(st.binom.cdf(k,n,p),st.binomtest(k,n,p,alternative='less'))

