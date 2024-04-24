import numpy as np 
import sklearn.linear_model as lm
import sklearn.model_selection as ms
from sklearn.metrics import r2_score
import scipy.optimize as opt
x=np.random.multivariate_normal(np.zeros(20),np.eye(20),100)
i=[]
while len(i)<4:
    temp=np.floor(20*np.random.sample())
    if temp not in i:
        i.append(int(temp))
    else:
        continue

a=np.random.normal(0,0.25,4)

y=x[:,i].dot(a)+np.random.normal(0,0.01,100)
print(i)
print(a)

betaols=np.linalg.inv(x.T@x)@(x.T@y)
print("highest five beta,",np.argsort(-1*np.abs(betaols))[:5])
# np.argsort(-1*np.abs(betaols))[5]
# model=lm.LinearRegression(fit_intercept=False).fit(x,y)
# model.coef_[i]
# model.intercept_
alpha=20
betaridge=np.linalg.inv(x.T@x+alpha*np.eye(x.shape[1]))@(x.T@y)
print("highest five beta for ridge,",np.argsort(-1*np.abs(betaridge))[:5])

r_sq=lambda x,y,beta:1-((y-x@beta).T@(y-x@beta))/((y-np.mean(y)).T@(y-np.mean(y)))
r_sq(x,y,beta=betaols)
r_sq(x,y,beta=betaridge)


# modelridge=lm.Ridge(alpha=20,fit_intercept=False).fit(x,y)
# modelridge.score(x,y)
# np.argsort(-1*np.abs(modelridge.coef_))[:5]

# mridge=lm.Ridge()
# par={"alpha":[1, 2, 5, 10, 20, 50, 100, 1000, 10000]}
# mridgecv=ms.GridSearchCV(mridge,par)
# mridgecv.fit(x,y)
# np.argsort(-1*np.abs(mridgecv.coef_))[:5]

obj=lambda beta,x,y,alpha: (y-x@beta).T@(y-x@beta)/(2*x.shape[0])+alpha*np.sum(np.abs(beta))
alpha=0.2
betalasso=opt.fmin(obj,x0=np.zeros(x.shape[1]),args=(x,y,alpha),maxiter=int(1e4))

print("highest five beta for lasso,",np.argsort(-1*np.abs(betalasso))[:5])

mlasso=lm.Lasso(fit_intercept=False,alpha=.2,max_iter=int(1e4)).fit(x,y)
np.argsort(-1*np.abs(mlasso.coef_))[:5]
mlasso.score(x,y)
r_sq(x,y,betalasso)
# i[np.argsort(-np.abs(a))]