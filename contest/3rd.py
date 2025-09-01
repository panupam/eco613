import numpy as np 
x=int(input())
y=input().split()
y=np.array([int(i) for i in y])
z=[]
for i in y:
    if np.sum(((y%i)==0))==i:
        z.append(i)

print(np.max(z))