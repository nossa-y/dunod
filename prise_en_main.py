##exo 1

def calcul_base_10(n):
    L=[]
    P=[]
    r = 1
    while r>0:
        r=n%10
        if r != 0:
            L.append(r)
            n=n//10
    m=len(L)
    for i in range (m):
        P.append(L[m-(i+1)])
    return P

#print(calcul_base_10(1234))

def somcube(n):
    s = 0
    L = calcul_base_10(n)
    m = len(L)
    for i in range (m):
        s += L[i]**3
    return s

#print(somcube(123))

"""for i in range (1000):
    if i==somcube(i):
        print (i)"""

def somcube2(n):
    nstr = str(n)
    L = []
    s = 0
    for elt in nstr:
        L.append(elt)
        s += int(elt)**3
    return L, s

#print(somcube2(123))

## exo 2

import numpy as np

def f(x):
    return np.sin(x) - x


X1 = [i for i in range(10,30)]
#print(X1)

Y1 = [np.sin(i)-i for i in X1]
#print(Y1)

def X2():
    L = np.zeros((20))
    pas = 20/19
    min=10
    for i in range (20):
        L[i] = 10 + pas*i
    return L

#print(X2()) "X2" est une fonction ici donc on écrit X2()


Y2 = f(X2())
print(Y2)

X3 = np.linspace(10, 30, 20)
#print(X1)

Y3=f(X1)
#print(Y1)





    
