import pandas as pd
import numpy as np
from pandas import DataFrame,Series

x=np.arange(12).reshape(3,4)
print(x)
print(np.ravel(x, order='C')) # 2차원 ->1차원 default=col방향으로
    #ravel : 다차원 배열 -> 1차원 배열
print(np.ravel(x,order='F'))
print(np.ravel(x,order='K')) #메모리 저장 순서 (사용 x)

y=np.arange(12).reshape(2,3,2)
print(y)
print(np.ravel(y,order='C'))

import matplotlib.pyplot as plt
# plt.plot([1,2,3,4],[1,4,9,16],'ro')
# plt.ylabel('some numbers')
# plt.show()

data={
    'a':np.arange(50),
    'c':np.random.randint(0,50,50),
    'd':np.random.randn(50)
}
data['b']=data['a']+10*np.random.randn(50)
data['d']=np.abs(data['d'])*100
print(data)
#
# plt.scatter('a','b',c='b',s='d', data=data)
# plt.xlabel('entry a')
# plt.ylabel('entry b')
# plt.show()


mu,sigma =100,15
x=mu+sigma*np.random.randn(10000)

n,bins,patches = plt.hist(x,bins=50) #bins =50 : 막대바가 50개 // density =1 밀도가 1
plt.title("histogram")
# plt.axis([40,160,0,0.03])
plt.grid(True)
plt.show()