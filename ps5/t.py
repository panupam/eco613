import numpy as np 
a=np.array([[1,0],[0,1]])
a[[0,1]]=a[[1,0]]
print(a)
