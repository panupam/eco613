import numpy as np 
import matplotlib.pyplot as plt

m1=np.random.multivariate_normal((1,0),[[1,0],[0,1]],10)
m2=np.random.multivariate_normal((0,1),[[1,0],[0,1]],10)
x=np.zeros((200,2))
y=np.ones(200)
y[100:]=-1*np.ones(100)
for i in range(10):
    x[10*i:10*i+10]=np.random.multivariate_normal(m1[i],[[0.1,0],[0,0.1]],10)
    x[10*(10+i):10*(10+i)+10]=np.random.multivariate_normal(m2[i],[[0.1,0],[0,0.1]],10)

plt.scatter(x[y==1,0],x[y==1,1],c="blue")
plt.scatter(x[y==-1,0],x[y==-1,1],c="red")
plt.show()
# print(x)

