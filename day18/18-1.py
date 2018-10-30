import pandas as pd
import numpy as np
from pandas import DataFrame,Series
import matplotlib.pyplot as plt

df=DataFrame({
    'a':['a1','a1','a2','a2','a3','a3'],
    'b':['b1','b1','b1','b1','b2',np.nan],
    'c':[1,1,3,4,4,4]
})
print(df['a'].unique()) #중복되는 값 제외
print(df['b'].unique()) #중복되는 값 제외
print(df['c'].unique()) #중복되는 값 제외

print(df['a'].value_counts()) #유일한 값들이 각각 몇개 있냐?
print(df['b'].value_counts()) #유일한 값들이 각각 몇개 있냐?
print(df['c'].value_counts()) #유일한 값들이 각각 몇개 있냐?

print(df['c'].value_counts(normalize=True))
print(df['c'].value_counts(sort=True,ascending=False)) #내림차순 정렬
print(df['c'].value_counts(sort=True,ascending=True)) #오름차순 정렬
print(df['c'].value_counts(sort=False)) #정렬 x

print(df['b'].value_counts(dropna=False)) #nan값도 확인
print(df['b'].value_counts(dropna=True))

print(df['c'].value_counts())
print(df['c'].value_counts(sort=False))
print(df['c'].value_counts(bins=[0,1,2,3,4,5],sort=False)) # 구간을 나눠서 그 범위안에 몇개 있나?

#표준화 : 변수들간의 scale(척도)이 서로 다른 경우, 직접적 상호간 비교를 할 수 없음.
#기계학습 모델링하는 과정에서 문제가 발생, 모델을 만들었다 하더라도 정확한 예측을 기대하기 어려움
#모델링 하기 앞서 변수들 간 척도가 다른 경우=> 표준화
#모집단이 정규분포에 따르는 경우,평균 :0, 표준편차:1 인 표준정규분포


data =np.random.randint(30,size=(6,50))
print(data)
print(np.mean(data,axis=1)) #행단위 평균

from numpy import *

data= np.random.randint(30,size=(6,5))
print(data)
print((data-mean(data, axis=0))/ std(data,axis=0)) #std() :표준편차, mean() :평균

import scipy.stats as ss
data_standardized_ss=ss.zscore(data) # ==같은 결과 : print((data-mean(data, axis=0))/ std(data,axis=0))
print(data_standardized_ss)

from sklearn.preprocessing import StandardScaler
ds = StandardScaler().fit_transform(data)  #==같은 결과 : print((data-mean(data, axis=0))/ std(data,axis=0))
print(ds)

print('-'*30)
#X~N(0,1) 표준화
#조건: 정규분포 따름, 이상치(특이값,outlier)가 없음
#z=(x-mean)/std
# IQR(InterQuantileRange): 3사분위수(75%)-1사분위수(25%)
# 데이터 100개를 오름차순 정렬

#이상치가 섞여있는 데이터르 표준화 하는 방법
# 1. 이상치를 제거한 후 표준화 수행 -> 분석,모델링
# 2. 중앙값, IQR을 사용해서 표준화

from sklearn.preprocessing import StandardScaler, RobustScaler
np.random.seed(777)
mu,sigma = 10,2 #mu => 임의 평균, sigma=>임의 표준편차
x=mu+sigma*np.random.randn(100)
print(x)
# plt.hist(x)
# plt.show()

print(np.mean(x))
print(np.std(x))

x[98:100]=100
print(x)

print(np.mean(x))
print(np.std(x))

# plt.hist(x,bins=np.arange(0,102,2))  # 따로 떨어진 막대그래프 =이상치가 된다.
# plt.show()

x=x.reshape(-1,1) #100행 1열 ##행자리 -1 : 행은 알아서 정하고 , 열자리 2: 두개로 나눠라/ 열자리 3 : 안나눠져서 애러가 나옴
print(x.shape)
print(x[0:10])

#standardscaler를 이용한 정규분포 표준화 작업
xss=StandardScaler().fit_transform(x)
print(xss)

# plt.hist(xss)
# plt.show()

xss_in=xss[xss<5]
print(xss_in)

plt.hist(xss_in,bins=np.arange(-3.0,3.0,0.2))
# plt.show()

print(median(x)) #중앙값 : 9.917732674869148
print(mean(x)) #평균 : 11.79720227993895
Q1=percentile(x, 25,axis=0) # 1사분위수 :8.77436132
Q3=percentile(x, 75,axis=0) # 1사분위수 :11.39649887
print(Q1)
print(Q3)


#이상치가 포함된 데이터의 중앙값과 iqr을 이용해서 표준화
x_rs= RobustScaler().fit_transform(x)
print(x_rs[-10:])
print(np.median(x_rs))
print(np.mean(x_rs))
print(np.std(x_rs))

x_rs_in = x_rs[x_rs<5]
plt.hist(x_rs_in,bins=np.arange(-3,3,0.2))
plt.show()