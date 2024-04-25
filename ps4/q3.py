import pandas as pd 
import numpy as np 
import sklearn.ensemble
import sklearn.model_selection as sklms
import sklearn.tree as tree
import sklearn 

car=pd.read_csv("ps4/Carseats.csv")
car.head()
car['US']=="Yes"
car["US"][car['US']=="Yes"]=1
car["US"][car['US']=="No"]=0

car["Urban"][car["Urban"]=="Yes"]=1
car["Urban"][car["Urban"]=="No"]=0

car["ShelveLoc"][car["ShelveLoc"]=="Good"]=1
car["ShelveLoc"][car["ShelveLoc"]=="Medium"]=0
car["ShelveLoc"][car["ShelveLoc"]=="Bad"]=-1

sum(car["US"])
sum(car['US']==1)
car=car.drop("Unnamed: 0",axis=1)
car.columns

for i in car.columns:
    car[i]=pd.to_numeric(car[i])

car.dtypes
x_train,x_test,y_train,y_test=sklms.train_test_split(car[car.columns[1:]],car["Sales"],test_size=0.2)


model=tree.DecisionTreeRegressor(max_leaf_nodes=10)
model.fit(x_train,y_train)
tree.plot_tree(model)

model.score(x_test,y_test)
 
model2=sklearn.ensemble.RandomForestRegressor(B=100,)