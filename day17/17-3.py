import numpy as np
import pandas as pd
from pandas import DataFrame, Series

df=DataFrame(np.random.randn(5,4),columns=['c1','c2','c3','c4'])
print(df)

df.ix[2,'c2']=np.nan
df.ix[[0,1],'c1']=None
print(df)

df_drop_row =df.dropna(axis=0) #nan이 포함된 행 제거
print(df_drop_row)

df_drop_column =df.dropna(axis=1) #nan이 포함된 열 제거
print(df_drop_column)

print(df['c1'].dropna())
print(df[['c1','c2','c3']].dropna(axis=1))
print('-'*30)
print(df.ix[[2,4],['c1','c2','c3']].dropna(axis=0)) #특정 행열을 제거

datestrs=['9/11/2018','9/13/2018','9/14/2018','9/20/2018']
dates=pd.to_datetime(datestrs)
print(dates)

ts=Series([1,np.nan,np.nan,10],index=dates)
print(ts)
ts_intp_linear=ts.interpolate()
print(ts_intp_linear)
ts_intp_linear=ts.interpolate(method='time') # method='time' : 시간의 흐름에 따라 보관
print(ts_intp_linear)

df=DataFrame({'c1':[1,np.nan,np.nan,10],
             'c2':[1, 3, np.nan, 10]})
df_v=df.interpolate(method='values')
print(df_v)

#fillna : 결측값 대체
#replace : 결측값 대체, 모든 값 대체
print('-'*30)
ser = Series([1,2,3,4,np.nan])
print(ser)
# ser=ser.replace(2,20)
# print(ser)
# ser=ser.replace(np.nan,5)
# print(ser)

print(ser.replace([1,2,3,4,np.nan],[6,7,8,9,10]))
print(ser.replace({
    1:6,
    2:8,
    3:9,
    4:7,
    np.nan:10}))

df=DataFrame({'c1':['a_old','b','c','d','e'],
              'c2':[1,2,3,4,5],
              'c3':[6,7,8,9,np.nan]})
print(df)
print(df.replace({'c1':'a_old'},{'c1':'a_new'}))
print(df.replace({'c3':np.nan},{'c3':10}))

#중복데이터 처리
data = {'key1':['a','b','b','c','c'],
        'key2':['v','w','w','x','y'],
        'col':[1,2,3,4,5]}
df=pd.DataFrame(data)
print(df)

print(df.duplicated(['key1'],keep='first'))
print(df.duplicated(['key1'],keep='last'))

#1개만 남기고 나머지 중복은 제거

print('='*30)
print(df)
print(df.drop_duplicates(['key1'],keep='first')) #앞쪽에서부터 중복값 확인
print(df.drop_duplicates(['key1'],keep='last')) # 뒷쪽에서부터 중복값 확인
print(df.drop_duplicates(['key1'],keep=False)) # 중복값은 모두 제거