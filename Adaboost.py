import numpy as np
import math as mt
def GetClassfyError(w,y,X,g):
    m=len(w)
    e=0
    for i in range(m):
        if g[i]!=y[i]:
            e=e+w[i]
    return e
def NewWeight(w,y,X,g,alpha):   
    Z=0
    m=len(w)
    temp=np.zeros(m)
    for i in range(m):
        temp[i]=w[i]*mt.exp(-alpha*y[i]*g[i])
    for i in range(m):
        Z=Z+temp[i]
    temp=temp/Z
    return temp
def judge(g,y,m):
    for i in range(m):
        if g[i]!=y[i]:
            return 0
    return 1
'''X为原数据 m行n列,每一行是一条数据，每条数据若是一维X搞成列向量'''
'''AdaBoost对已经存在的参数列表coff和函数列表sumG操作,不返回'''
'''getG为自定义的在权重D和数据集X,y返回一个分类器G的方法，G对X操作得到分类结果向量g'''
def AdaBoost(X,y,getG,sumG,coeff):
   si=0
   m=X.shape[0]
   D=np.ones(m)
   D=D/m
   G=getG(D,X,y)
   sumG.append(G)
   g=G(X)
   if judge(g,y,m)==1:
       coeff.append(1)
       return   
   e=GetClassfyError(D,y,X,g)
   alpha=mt.log((1-e)/e)/2
   D=NewWeight(D,y,X,g,alpha)
   coeff.append(alpha)
   ti=0
   while si==0:
         G = getG(D, X, y)
         g = G(X)
         e=GetClassfyError(D,y,X,g)
         alpha=mt.log((1-e)/e)/2
         D=NewWeight(D,y,X,g,alpha)
         sumG.append(G)
         coeff.append(alpha)
         def tpG(X):
             s=np.zeros(m)
             for i in range(len(coeff)):
                 s=s+coeff[i]*sumG[i](X)
             for i in range(m):
                 s[i]=np.sign(s[i])
             return s
         g=tpG(X)
         if judge(g,y,m)==1:
             si=1
         ti=ti+1
   return
