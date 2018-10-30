import pandas as pd
from pandas import DataFrame as df

#concat(): 파이썬 데이터프레임 합치는 작업 = rbind,cbind: R언어

df_1=df({
    'a':['a0','a1','a2'],
    'b': ['b0', 'b1', 'b2'],
    'c': ['c0', 'c1', 'c2'],
    'd': ['d0', 'd1', 'd2']},index=[0,1,2])

df_2=df({
    'a':['a3','a4','a5'],
    'b': ['b3', 'b4', 'b5'],
    'c': ['c3', 'c4', 'c5'],
    'd': ['d3', 'd4', 'd5']},index=[3,4,5])

print(df_1)
print(df_2)

df_12_axis0=pd.concat([df_1,df_2]) # 위아래로 합치기
print(df_12_axis0)

df_3=df({
    'e':['e0','e1','e2'],
    'f': ['f0', 'f1', 'f2'],
    'g': ['g0', 'g1', 'g2'],
    'h': ['h0', 'h1', 'h2']},index=[0,1,2])

df_13_axis1=pd.concat([df_1,df_3],axis=1) #좌우로 합치기
print(df_13_axis1)

df_4=df({
    'a':['a0','a1','a2'],
    'b': ['b0', 'b1', 'b2'],
    'c': ['c0', 'c1', 'c2'],
    'e': ['e0', 'e1', 'e2']},index=[0,1,3])
print('-'*30)
#df1과 df4를 outer_join(외부 조인) 수행
print(df_1)
print('-'*30)
print(df_4)
print('-'*30)
    #위아래로 합쳐짐
df_14_outer=pd.concat([df_1,df_4],join='outer') #열끼리 합쳐지고 값이 없는 자리는 NaN이 들어간다. 두데이터프레임의 컬럼에 대한 합집합(아웃터조인)
print(df_14_outer)
df_14_inner=pd.concat([df_1,df_4],join='inner') # 공통된 변수값을 가지는 값만 남겨둔다. 두데이터프레임의 컬럼에 대한 교집합(이너조인)
print(df_14_inner)

print('-'*30)
print(df_1)
print(df_4)
    #좌우로 합쳐짐
df_14_outer_axis1=pd.concat([df_1,df_4],join='outer',axis=1) #합집합
print(df_14_outer_axis1)
df_14_inner_axis1=pd.concat([df_1,df_4],join='inner',axis=1) #교집합
print(df_14_inner_axis1)

print('-'*30)
df_14_join_axis=pd.concat([df_1,df_4],join_axes=[df_1.index],axis=1) #df_1의 index를 기준으로 합쳐라.