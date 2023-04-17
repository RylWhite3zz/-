import numpy as np
'''小于某个阈值取-1反之取1，阈值不取到某个x，此处X为一维向量'''
'''阈值判定是个特例，'''

def threshold(D,X,y):
    n=len(D)
    sign=0
    minn=2
    sorted(X)
    e=0
    category=0
    temp=np.ones(n)
    temp=-1*temp


    for j in range(n):
        if y[j] != temp[j]:
            e = e + D[j]
    sign=0
    category=1
    minn = min(e, minn)
    e = 0
    for i in range(n):
        temp[i]=1
        for j in range(n):
            if y[j]!=temp[j]:
               e=e+D[j]
        if minn>e:
           sign=i
        minn=min(e,minn)
        e=0



    temp = np.ones(n)
    for j in range(n):
        if y[j] != temp[j]:
            e = e + D[j]
    if minn > e:
        sign = 0
        category=1
    minn = min(e, minn)
    e = 0
    for i in range(n):
        temp[i]=-1
        for j in range(n):
            if y[j]!=temp[j]:
               e=e+D[j]
        if minn>e:
           sign=i
           category=1
        minn=min(e,minn)
        e=0
    if sign==n:
       v=X[n-1][0]+1
    elif sign==0:
        v=X[sign][0]-1
    else :
        v=(X[sign][0]+X[sign+1][0])/2

    print("category:")
    print(category)
    print("location:")
    print(sign)
    def gettg1(X):
        v2 = v
        G = np.zeros(n)

        for i in range(n):

            if X[i][0] < v2:
                G[i] = -1
            else:
                G[i] = 1
        return G
    def gettg(X):
        v1=v
        G=np.zeros(n)

        for i in range(n):

            if X[i][0]<v1:
                G[i]=1
            else :
                G[i]=-1
        return  G

    if category==0:
        return gettg
    else:
        return gettg1