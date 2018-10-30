    # 정규화 : 최소값, 최대값 이용. 범위 : 0~1
#딥러닝(인공신경망)
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, minmax_scale, Binarizer, binarize

    #           중간  기말  등수
X=np.array([[10., -10., 1.],
          [5., 0., 2.],
          [0., 10., 2.]])

print((X-X.min(axis=0))/(X.max(axis=0)-X.min(axis=0)))  # 결과값이 0 = 최소값일 경우, 1=최대값일 경우 나오는 값

mms=MinMaxScaler()
xmms=mms.fit_transform(X)  #같은 결과 ==(X-X.min(axis=0))/(X.max(axis=0)-X.min(axis=0))
print(xmms)

xmms2= minmax_scale(X, axis=0,copy=True)  #같은 결과 ==(X-X.min(axis=0))/(X.max(axis=0)-X.min(axis=0))
print(xmms2)

#이진화(0,1): 연속형 변수값 -> 0또는 1로 변환
#임계값(threshold)변환 기준 값

#당뇨병 유/무 판정하기.

X=np.array([[10.,-10.,1.],
            [2.,3.,1.7],
            [0.,10.,3.]])
binarizer=Binarizer().fit(X) #복사본을 이용하겠다/
print(binarizer)
print(binarizer.transform(X)) #이진화 0보다 작거나 같은 값 =0, 0보다 크거나 같은 값 =1 로 표현

binarizer=Binarizer(threshold=2.0) # 2보다 작은지 큰지를 구분하여 이진화.
print(binarizer)
print(binarizer.transform(X))

print(binarize(X, threshold=2.0,copy=False))
print(X)

print('-'*30)
#범주형 변수 -> 이진화
#성별 : 남(0), 여(1) 로 인코딩 하겠다.
#연령 : 20대(0), 30대(1), 40대(2),50대(3)로 인코딩 하겠다.
#성적 : A(0), B(1),...F(5)로 인코딩 하겠다.
    # ID 성별 연령대 성적
    # 1     0   0   1
    # 2     1   3   0
    # ...=> 범주형 데이터는 원핫인코딩을 해줘야한다. ==> 원핫인코딩 과정을 거치지 않으면 일반 숫자사이의 관계가 생겨버려 다른 자료에 영향을 줌.
    # 성별(0,1)=> 0:10, 1:01
    # 연령대 (0~3) =>0:1000, 1:0100,2:0010,3:0001
    # 성적 (0~5) =>0:100000, 1:010000, 2:001000 ....

# ex) 번호판 판별기
# 1)원핫 인코딩
#     5: 0000010000
#     4: 0000100000
# 가
# 1
# 2
# 3
# 4
#
# 2) 코드를 판별기에 입력(5)
# 3) 판별기는 판별 결과를
#     0 0 0.05 0 0 0.9 0.05 0 0 0 (0~9 까지의 숫자일 확률을 표시)
#     0000010000 =>5 이렇게 표현

from sklearn.preprocessing import OneHotEncoder
                #성별(2), 연령대(3),성적(5) 의 종류로 데이터 구분됨.
data_train =np.array([[0,0,0],
                      [0,1,1],
                      [0,2,2],
                      [1,0,3],
                      [1,1,4]])
enc=OneHotEncoder()
print(enc.fit(data_train))
print(enc.active_features_)
    #[0 1 2 3 4 5 6 7 8 9]
    #남여, 20,30,40대, 성적(ABCDF)  ==>성별 범주는 2개, 연령대범주는 3개, 등급 볌주는 5개
print(enc.n_values)
print(enc.feature_indices_)  #[ 0  2  5 10] :성별 0이상 2미만 , 연령대 2이상 5미만, 성적 5이상10미만

#여성(1),40대(2), 등급D(3)
data_new=np.array([[1,2,3]])
print(enc.transform(data_new).toarray()) #[[0. 1. =여성(1)//0. 0. 1.=40대(2)// 0. 0. 0. 1. 0.=등급D(3)]]