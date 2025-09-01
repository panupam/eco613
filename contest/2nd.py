import numpy as np
x=int(input())
y=int(input())
z=int(input())
p=np.array([x,y,z])
sum=np.sum(p//3)
sum+=np.min(p%3)
print(sum)