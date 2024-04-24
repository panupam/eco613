import numpy as np 
import sklearn.neural_network as nn
import sklearn.model_selection as ms
import matplotlib.pyplot as plt 


x=np.random.uniform(-10,10,(10000,2))
print(x.shape)
y=np.sum(x*x,axis=1)
mod=nn.MLPRegressor(solver='adam',max_iter=1000)
par={"hidden_layer_sizes":[5, 10, 20, 50, 100],'activation':['relu','tanh','logistic']}
modcv=ms.GridSearchCV(mod,par).fit(x,y)
modcv.score(x,y)

x_test=np.random.uniform(-10,10,(10000,2))

y_test=np.sum(x_test*x_test,axis=1)
modcv.score(x_test,y_test)