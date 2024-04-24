import numpy as np 
import sklearn.neural_network as nn
import sklearn.model_selection as ms
import matplotlib.pyplot as plt 
from ucimlrepo import fetch_ucirepo 
import keras as kr
from sklearn.metrics import r2_score
# fetch dataset 
spambase = fetch_ucirepo(id=94) 
  
# data (as pandas dataframes) 
X = spambase.data.features 
y = spambase.data.targets 
  
# metadata 
print(spambase.metadata) 
  
# variable information 
print(spambase.variables) 

x_train,x_test,y_train,y_test=ms.train_test_split(X,y,test_size=.25)
mod=nn.MLPClassifier()
par={"hidden_layer_sizes":[5, 10, 20, 50, 100],'activation':['relu','tanh','logistic']}

modcv=ms.GridSearchCV(mod,par).fit(x_train,y_train["Class"])
print("For Training data, score")
modcv.score(x_train,y_train['Class'])
print("For testing data, score")
modcv.score(x_test,y_test["Class"])
modcv.best_params_
par={"ut":[5, 10, 20, 50, 100],'act':['relu','tanh','sigmoid']}
modkr=kr.models.Sequential( [kr.layers.Input(shape=(57,)),
                             kr.layers.Dense(units=200,activation="tanh"),
                             kr.layers.Dense(1,activation="sigmoid")
                             ]
)
modkr.compile(loss=kr.losses.BinaryCrossentropy(),optimizer="adam")
modkr.fit(x_train,y_train['Class'])
y_hat=modkr.predict(x_train)
y_pred=np.array((y_hat>0.5).T[0],dtype=int)
# r2_score(y_train,y_pred)
# y_hat>0.5
# y_hat=modcv.predict(x_test)