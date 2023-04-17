import numpy as np
import  Adaboost
import GetG
a=[1,2,3,4,5,6,7]
X=np.array(a)
X=X.reshape((len(X),1))
y=[1,1,-1,-1,1,1,-1]
A=[]
B=[]
C=[]
D=[]
getG=GetG.threshold
Adaboost.AdaBoost(X,y,getG,A,B)
y[-1]=1
print(B)