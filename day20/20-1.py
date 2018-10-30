    #데이터프레임의 문자열 컬럼들-> 합치는 등의 작업 -> 새로운 컬럼
import pandas as pd
import numpy as np
from pandas import DataFrame,Series

    #format 함수 사용 연습
# x=3.141592
# print("{:.2f}".format(x))
# print("{:+.2f}".format(x))
# x=-3.141592
# print("{:+.2f}".format(x))
# x=2.718
# print("{:.0F}".format(x)) # 첫째자리에서 반올림
# x=5
# print("{:0>2d}".format(x)) # 너비:2, 0으로 채워라
# x=7777777
# print("{:>5d}".format(x)) #너비 5, 0으로 채워라
#
# print("{:,}".format(x))
# x=0.25
# print("{:.2%}".format(x))

df=pd.DataFrame({'id':[1,2,10,20,100,200],
              'name':['aaa','bbb','ccc','ddd','eee','fff']})
print(df)

df['id_2']=df['id'].apply(lambda x:"{:0>5d}".format(x)) #id를 다섯 자리 수로 표현
print(df)

df['id_name']=df[['id_2','name']].apply(lambda x:'_'.join(x),axis=1)
print(df)

df['id_3']=df['id'].apply(lambda x:"{:.2f}".format(x))
print(df)
#id_name_3 컬럼 추가
#1.00:AAA
df['name_3']=df['name'].apply(lambda x:x.upper())
print(df)
df['name_3']=df[['id_3','name']].apply(lambda x:':'.join(x),axis=1)
print(df)

    #groupby 집계함수
#1. 딕셔너리를 이용한 그룹화
df=DataFrame(data=np.arange(20).reshape(4,5),
             columns=['c1','c2','c3','c4','c5'],
             index=['r1','r2','r3','r4'])
print(df)

mdr = {'r1':'row_g1',
       'r2': 'row_g1',
       'r3': 'row_g2',
       'r4': 'row_g2'}
gbr=df.groupby(mdr)
print(gbr.sum())

mdc = {'c1':'col_g1',
       'c2': 'col_g1',
       'c3': 'col_g2',
       'c4': 'col_g2',
       'c5': 'col_g2'}
gbc=df.groupby(mdc,axis=1)
print(gbc.sum())

#dict -> Series 변경
print(type(mdr))
print(mdr)
msr=Series(mdr)
print(type(msr))
print(msr)

msc=Series(mdc)
print(msc)

#2. Series를 이용한 그룹화
print(df.groupby(msr).sum())
print(df.groupby(msc,axis=1).sum())

#함수를 이용한 그룹화 ---> 비효율적!
def rgf(x): #df에 대한 정보가 x에 전달
    if x=='r1' or x=='r2':
        rg='row_g1'
    else:
        rg='row_g2'
    return rg
print(df.groupby(rgf).sum())