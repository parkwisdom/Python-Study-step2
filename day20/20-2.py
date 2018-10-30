    # 연속형 변수 -> 기술통계량 집계 함수
# 그룹화 : 딕셔너리 / 시리즈 / 함수 ==>그룹만듬

import pandas as pd
import numpy as np
from pandas import DataFrame,Series
df= DataFrame({'group':['a','a','a','b','b','b'],
               'value_1':np.arange(6),
               'value_2':np.random.randn(6)})
print(df)
grouped=df.groupby('group') # 'group'을 기준으로 그룹화!
print(grouped)

print(grouped.count()) #a,b 각각의 그룹에 값이 몇개씩 있는지.명확한 계산 방법은 non_NA개수가 출력이 되는 것임.
print(grouped.sum())  #DataFrame
print(grouped['value_2'].sum()) #Series
#Series ->DataFrame
df2=DataFrame(grouped.sum()['value_2'])
print(type(df2)) #DataFrame

print('-'*30)
print(df)
print(grouped.min()) #최소
print(grouped.max()) #최대
print(grouped.mean()) #평균
print(grouped.median()) # 중앙값
print(grouped.std()) #표준편차
print(grouped.var()) #분산
print(grouped.quantile(0.5)) #분위수 (0~1사이의 값)
# 각 그룹별 최소값~최대값에 대해 지정된 위치값을 추출 a: 0~2, b:3~5  =>0.5 =50%위치
print(grouped.first()) # 그룹내 첫번째값
print(grouped.last()) # 그룹내 마지막값

    #그룹별 기술통계량
print(grouped.describe()['value_1']) #===> 데이터 요약 정리 // count  mean  std  min  25%  50%  75%  max
print(grouped.describe()['value_1'].T)


def iqr_func(x):
    q3,q1=np.percentile(x,[75,25])
    iqr=q3-q1
    return iqr
print(grouped.aggregate(iqr_func)) #aggregate: 내가 만든 집계함수를 정의하고 싶을 때
print(grouped.agg(iqr_func))

print(grouped.quantile([0.75,0.25]))


df=DataFrame({
    'name':['kim','KIM','Kim','lee','LEE','Lee','park','choi'],
    'value':[1,2,3,4,5,6,7,8],
    'value_2':[100,300,200,100,100,300,50,80]})
print(df)

#name컬럼 값 -> 새로운 컬럼 생성('kim','lee','others')

name_mapping={
    'Kim': 'kim',
    'KIM': 'kim',
    'Lee': 'lee',
    'LEE': 'lee',
    'park': 'others',
    'choi':'others'
}
func=lambda x:name_mapping.get(x,x)
print(df)

df['name_2']=df.name.map(func)
print(df.groupby('name_2').sum())

print(df.groupby(['name_2','name'])['value_2'].sum())

print('='*40)
x=np.arange(18).reshape(3,6)
print(x)

print(np.hsplit(x,3))  #수평방항으로 나누기/
print(np.hsplit(x,(2,4))) # == x[:,0:2],x[:,2:4],x[:,4:6] ==np.hsplit(x,3)
print(np.split(x,3,axis=1)) #==np.hsplit(x,3)
print('-'*40)
x1,x2,x3=np.hsplit(x,3)
print(x1)

print('='*40)
print(x)
print(np.vsplit(x,3)) #수직?방향으로 나누기

#np.argmin(), np.argmax()-->해당값의 위치가 나옴
#np.min

print('='*40)
x=np.array([15,14,13,12,11,10])
print(x.min())
print(x.max())
print(np.max(x))
print(x.argmin())
print(x.argmax())
print(np.argmax(x))

x=np.array([15,14,13,12,11,10])
#x배열에서 13 이상인 색인의 위치를 출력
print(np.where(x>=13))
#x배열에서 13이상인 값들을 출력(15,14,13)
print(x[np.where(x>=13)])
#x배열에서 13이상의 값은 모두 100으로 치환하여 x배열을 출력
print(np.where(x>=13,100,x))

x2=[]
for i in list(x):
    if i>=13:
        x2.append(100)
    else:
        x2.append(i)
print(x2)
x2=np.asarray(x2) # list->array
print(x2)

x=np.array([1,2,3,1,2,4])
print(np.unique(x))

x=np.array([1,2,3,4])
y=np.array([3,4,6,5])
print(np.intersect1d(x,y)) #교집합
print(np.union1d(x,y)) #합집합
print(np.setdiff1d(x,y)) #x의 차집합
print(np.setxor1d(x,y)) # xy의 차집합

x=np.array([1,2,3,4,5,6])
y=np.array([2,4])
print(np.in1d(x,y)) #x와y의 교집합이 있는지 확인할때 사용

    #배열 합치기
#1) 왼쪽에서 오른쪽으로 합치기 =>1차원
# - np.r_[x,y] , np.hstack([x,y])
#2) 위에서 아래쪽으로 합치기 =>2차원
# - np.r_[[x],[y]], np.vstack([x,y])
#3) 두개의 1차원 배열 -> 세로로 합치기 =>2차원 배열
# - np.c_[x,y], np.column_stack([x,y])

a=np.array([1,2,3])
b=np.array([4,5,6])
print(np.r_[a,b]) #좌우로 합치기
print(np.hstack([a,b]))

print(np.r_[[a],[b]]) # 위아래로 합치기
print(np.vstack([a,b]))

print(np.shape(np.c_[a,b]))
print(np.column_stack([a,b]))
