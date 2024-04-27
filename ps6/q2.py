import statsmodels.tsa.arima.model as arima
import pandas as pd
import numpy as np
bjm=pd.read_csv("ps6/bjm.csv",header=None)


# data = pd.read_csv("../code/eco613/ps6/bjm.csv",header=None)
# data.head()
x = bjm.iloc[:, 1:3]  # Corrected indexing
# print(x)
m=np.inf
a,b=-1,-1
a,b,c,d,e=[],[],[],[],[]
for p in range(5):
    for q in range(5):
        model = arima.ARIMA(x[1], order=(p, 0, q))
        res = model.fit()
        a.append(p)
        b.append(q)
        c.append(res.aic)
        d.append(res.bic)
        e.append(res.hqic)
#         if m>res.bic:
#             a,b=p,q
#             m=res.bic
#        print([p, q, res.aic, res.bic, res.hqic])
model = arima.ARIMA(x.iloc[:,0],order=(2,0,3))
res=model.fit()
res.summary()
model = arima.ARIMA(x.iloc[:,0],order=(a[np.argmin(c)],0,b[np.argmin(c)]))
res=model.fit()
res.summary()
