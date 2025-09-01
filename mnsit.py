import tensorflow as tf
import keras as kr
import numpy as np 
(x_train,y_train),(x_test,y_test)=kr.datasets.mnist.load_data()
x_train=x_train.reshape((60000,784))
x_test=x_test.reshape((10000,784))
x_mean=np.zeros((10,784))
for i in range(10):
    x_mean[i]=np.average(x_train[y_train==i],axis=0)
y_hat=-1*np.ones(10000)
for i,z in enumerate(x_test):
    d=np.zeros(10)
    for j in range(10):
        d[j]=np.linalg.norm(x_mean[j]-z)
    y_hat[i]=np.argmin(d)
# np.sum(==y_test)
# np.ar
# y_test[0]
import matplotlib.pyplot as plt 
for i in range(10):
    plt.imshow(x_mean[i].reshape((28,28)),cmap='gray')
    plt.show()


x_mean[0].reshape((28,28))


# np.sum(np.array(np.argmax((x_test).dot(x_mean.T),axis=1),dtype=int)==y_test)
np.sum(y_hat==y_test)