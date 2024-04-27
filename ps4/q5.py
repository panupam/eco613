import numpy as np 
import sklearn.svm as svm 
import sklearn.model_selection as ms
import matplotlib.pyplot as plt

x=np.random.multivariate_normal(np.zeros(2),np.eye(2),200)

y=np.sign(x[:,0]+x[:,1])
par={"C":[1,10,100,1000,10000]}
m=svm.SVC(kernel="linear")
mcv=ms.GridSearchCV(m,par).fit(x,y)
mcv.best_params_
m.set_params(C=100)
m1=svm.SVC(kernel='linear',C=mcv.best_params_['C']).fit(x,y)
m.fit(x,y)
m.coef_
yl=-(m1.intercept_[0]+m1.coef_[0,0]*x[:,0])/m1.coef_[0,1]

x2=np.random.multivariate_normal(np.zeros(2),np.eye(2),200)
y2=m.predict(x2)

plt.scatter(x[y==1][:,0],x[y==1][:,1],c='red')
plt.scatter(x[y==-1][:,0],x[y==-1][:,1],c='blue')
plt.plot(x[:,0],yl)
# plt.

# plt.scatter(x2[np.sum(x2,axis=1)>0][:,0],x2[np.sum(x2,axis=1)>0][:,1],c='red')
# plt.scatter(x2[np.sum(x2,axis=1)<=0][:,0],x2[np.sum(x2,axis=1)<=0][:,1],c='blue')
# plt.plot(x[:,0],yl)


plt.show()


# m.set_params