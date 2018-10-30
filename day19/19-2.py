#데이터프레임 정렬 : DataFrame.sort_values()
#튜플 정렬 : sorted(tuple,key)
#리스트 정렬 : sort(), sortde()
import pandas as pd
# pdf=pd.DataFrame({'seq':[1,3,2],
#                   'name':['park','lee','choi'],
#                   'age':[30,20,40]})
# print(pdf)
# pdf.sort_values(by=['seq'], axis=0,ascending=False) #axis default=0
# pdf.sort_values(by=['seq'],axis=0,inplace=True)
# print(pdf)
#
import numpy as np
# pdf=pd.DataFrame({'seq':[1,3,2],
#                   'name':['park','lee','choi'],
#                   'age':[30,20,40]})
# pdf.sort_values(by=['seq'],axis=0,inplace=True,na_position='last')
# print(pdf)
#
# pt=[(1,'park',30),
#     (3, 'lee', 20),
#     (2, 'choi', 40)]
# print(pt)
# print(sorted(pt, key=lambda ptf:ptf[0]))
# print(sorted(pt, key=lambda ptf:ptf[1]))
# print(sorted(pt, key=lambda ptf:ptf[2]))
# print(sorted(pt, reverse=True,key=lambda ptf:ptf[1])) #내림차순
#
# print('-'*40)
# #리스트 : sort,sorted(list)
# mlist=[9,4,1,2,7]
# print(sorted(mlist))
# print(mlist)
#
# mlist.sort()
# print(mlist)

# print('-'*40)
# Seri = pd.Series([10.,11.,12.,13.,14.])
# print(Seri)
# print(Seri[3])
# print(Seri[:3])
# #평균값이 12이상인 행만 추출
# print(Seri[Seri.mean()<=Seri])
# print(Seri[[3,4,2]])
#
# print('-'*40)
# Seri_ix =pd.Series([10.,11.,12.,13.,14.],
#                    index=['a','b','c','d','e',])
# print(Seri_ix)
# print(Seri_ix[['c','d','b']])
# print(Seri_ix.get(['c','d','b']))
#
# Seri_ix['c']=100
# print(Seri_ix)
# print('c' in Seri_ix)
#
# #ix, loc, iloc
# #ix : 위치 지정하여 데이터를 참조, 레이블을 이용하여 데이터를 참조
#     #ix 속성에 수치값을 주는 경우에는 loc와 동일한 결과가 나온다.
# #loc  : 레이블을 이용하여 데이터 참조(위치x)
# #iloc : 위치 지정하여 데이터를 참조(레이블 x)
# print('-'*40)
# Seri = pd.Series(np.nan,index=[19,18,17,16,15,  1,2,3,4,5])
# print(Seri)
# print(Seri.iloc[:3]) #0번행 ~2번행까지 추출
# print(Seri.loc[:3]) #0~7번행까지 추출 --> 레이블을 기준으로 3이 나올때까지!!
# print(Seri.ix[:3])

print('-'*40)
from pandas import DataFrame
df=DataFrame({'c1':[0,1,2,3],
              'c2':[4,5,6,7],
              'c3':[8,9,10,np.nan]},index=['r1','r2','r3','r4'])
print(df.index)
print(df.columns)

df_r1=DataFrame(df, index=['r1','r3'])
print(df_r1)
df_c1=DataFrame(df, columns=['c1','c3'])
print(df_c1)
print(df)
#     c1  c2    c3
# r1   0   4   8.0
# r2   1   5   9.0 => 10   2
# r3   2   6  10.0 => 8   0
# r4   3   7   NaN
#기존의 데이터 프레임으로부터 원하는 특정부분만 추출하여 새로운 데이터프레임을 만듬
df_ex = DataFrame(df,index=['r3','r1'],columns=['c3','c1'])
print(df_ex)
#데이터프레임 참조
print(df['c1'])
print(df[['c1','c3']])
df['csum']=df['c1']+df['c2']
print(df)
df=df.assign(cmul=df['c1']*df['c2'])
print(df)
df=df.assign(cmul2=lambda x:x.c1 * x.c2)    #df-> x로 전달 -> x.c1 * x.c2 계산 ->cmul2에 대입 ->df에 내용추가
print(df)

# 데이터 삭제
print(df.drop(['cmul','cmul2'],1)) #['cmul','cmul2'],1  >>열을 지울때는 반드시 1을 넣어줘야함.
print(df.drop(['r1','r3']))

del df['csum']  # 데이터 삭제
print(df)

print('-'*40)
print(df[0:2])
print(df['c1'][0:2])
print(df.c1[0:2])

print(df.loc['r1'])

print(df.loc[['r1','r2']])
print(df.iloc[0:2])
print(df[0:2])
print(df[df['c1']<=1])

s=['c1','c2']
print(df[s])