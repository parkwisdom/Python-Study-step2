    #데이터프레임 결측값 처리
#pandas에서는 결측값: NaN, None
# import pandas as pd
from pandas import DataFrame as df

# df_left=df({
#     'a': ['a0', 'a1', 'a2','a3'],
#     'b': [0.5,2.2,3.6,0.4],
#     'key':['k0','k1','k2','k3']})
#
# df_right=df({
#     'c': ['c0', 'c1', 'c2','c3'],
#     'd': ['d0', 'd1', 'd2','d3'],
#     'key':['k2', 'k3', 'k4','k5']})
#
# df_all= pd.merge(df_left,df_right,how='outer',on='key')
# print(df_all)
#
# print(pd.isnull(df_all))
# print(df_all.isnull())
#
# print(pd.notnull(df_all))
# print(df_all.notnull())
# print('-'*40)
# df_all.ix[[0,1],['a','b']]=None #None 곤색 = 예약어 =>변수로 사용 안됨/
# print(df_all)
#
# print(df_all[['a','b']].isnull())
#
# print(df_all.isnull().sum())
#
# print(df_all['a'].isnull().sum())
#
# print(df_all.notnull().sum())
# print('-'*40)
# print(df_all)
# print(df_all.isnull().sum(1))
# print('-'*40)
# df_all['NaN_cnt']=df_all.isnull().sum(1)
# df_all['NotNull_cnt']=df_all.notnull().sum(1)
# print(df_all)
#
# #결측값 여부? isnull(),notnull()
# #열단위 결측값 개수 : df.isnull().sum()
# #행단위 결측값 개수 : df.isnull().sum(1)

#
# print('-'*40)
import numpy as np
df= df(np.arange(10).reshape(5,2),
       index=['a','b','c','d','e'],
       columns=['c1','c2'])
print(df)

df.ix[['b','e'],['c1']]=None
df.ix[['b','c'],['c2']]=None
print(df)
# print('-'*40)
# print(df.sum()) #NaN은 0으로 처리
# print('-'*40)
# print(df['c1'].sum())
# print('-'*40)
# print(df['c1'].cumsum())
# print('-'*40)
# print(df.mean()) #(0+4+6)/3, NaN은 제외됨
#

# print(df.mean(1)) #행기준 평균
# print(df.std())
#
# print(df)# df['c3']=df['c1']+df['c2']

# print(df)
# print('-'*40)
#
# from pandas import DataFrame
# df= DataFrame(np.arange(10).reshape(5,2),
#        index=['a','b','c','d','e'],
#        columns=['c1','c2'])
#
# df2=DataFrame({'c1':[1,1,1,1,1],
#         'c4':[1,1,1,1,1]},
#        index=['a','b','c','d','e'])
# df['c3']=df['c1']+df['c2']
# print(df)
# print(df2)

import numpy as np
import pandas as pd
from pandas import DataFrame
df=DataFrame(np.random.randn(5,3),
             columns=['c1','c2','c3'])

print(df)

df.ix[0,0]=None
df.ix[1,['c1','c3']]=np.nan # None
df.ix[2,'c2']=np.nan
df.ix[3,'c2']=np.nan
df.ix[4,'c3']=np.nan
print(df)

df_0=df.fillna(0)
print(df_0)

df_missing =df.fillna('missing')
print(df_missing)

print(df)
print(df.fillna(method='ffill')) #아래쪽으로 내려가면서 대체
print(df.fillna(method='pad'))
print(df.fillna(method='bfill')) #제일 뒷쪽에서부터 nan 값 넣음

print('='*40)
print(df)
print(df.fillna(method='ffill',limit=1 )) #limit=1 : nan 값을 윗쪽의 값으로 1개 대체해줌

print('='*40)
print(df)
print(df.mean())
print(df.fillna(df.mean())) #nan값을 평균값으로 대체

print('='*40)
print(df.where(pd.notnull(df),df.mean(),axis='columns')) #df에서 nall이 아닌 것의 cilumns의 평균을 구하여 nan값에 대체

# print(df.where(pd.notnull(df),df.mean(),axis='rows'))

print('='*40)
print(df.mean()['c1'])
print(df.fillna(df.mean()['c1']))
print('='*40)
print(df)
print(df.mean()['c1':'c2'])
print(df.fillna(df.mean()['c1':'c2']))

print('='*40)
df_2 = pd.DataFrame({'c1':[1,2,3,4,5,],
                     'c2':[6,7,8,9,10]})
df_2.ix[[1,3],['c2']]=np.nan
print(df_2)

df_2['c2_new']=np.where(pd.notnull(df_2['c2'])==True,df_2['c2'],df_2['c1'])  #c2값을 넣고 c2값이 nan인 경우 c1값을 넣어라
print(df_2)

