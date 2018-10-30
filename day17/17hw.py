import numpy as np
import pandas as pd
from pandas import DataFrame as df

# 1. 두 개의 데이터프레임을 만들고 merge 명령으로 합친다. 단 데이터프레임은 다음 조건을 만족해야 한다.
# -1.각각 5 x 5 이상의 크기를 가진다.
# -2.공통 열을 하나 이상 가진다.

df_a=df({
    'a':['a0','a1','a2','a3','a4'],
    'b': ['b0', 'b1', 'b2','b3','b4'],
    'c': ['c0', 'c1', 'c2','c3','c4'],
    'd': ['d0', 'd1', 'd2', 'd3','d4'],
    'e': ['e0', 'e1', 'e2', 'e3','e4']},index=[1,2,3,4,5])

df_b=df({
    'd': ['d0', 'd1', 'd2','d3','d5'],
    'e': ['e0', 'e1', 'e2','e3','e5'],
    'f':['f0','f1','f2','f3','f4'],
    'g': ['g0', 'g1', 'g2', 'g3', 'g4'],
    'h': ['h0', 'h1', 'h2', 'h3', 'h4']},index=[1,2,3,4,5])
print(df_a)
print(df_b)
# df_ab=pd.merge(df_a,df_b,left_index=True,right_index=True,how='left')
# print(df_ab)
# df_ab=pd.merge(df_a,df_b,left_index=True,right_index=True,how='right')
# print(df_ab)
# df_ab=pd.merge(df_a,df_b,left_index=True,right_index=True,how='outer')
# print(df_ab)
# df_ab=pd.merge(df_a,df_b,left_index=True,right_index=True,how='inner')
# print(df_ab)
df_ab=pd.merge(df_a,df_b,how='outer')
print(df_ab)

# 2.어느 회사의 전반기(1월 ~ 6월) 실적을 나타내는 데이터프레임과
# 후반기(7월 ~ 12월) 실적을 나타내는 데이터프레임을 만든 뒤 합친다.
# 실적 정보는 "매출", "비용", "이익" 으로 이루어진다. (이익 = 매출 - 비용).
#
# 또한 1년간의 총 실적을 마지막 행으로 덧붙인다.
com_fh =df({
    '매출':[100, 200,300,400,500,600],
    '비용':[60,140,250,300,390,430]},index=['1월','2월','3월','4월','5월','6월'])
# print(com_fh)
com_fh['이익']=com_fh['매출']-com_fh['비용']
print(com_fh)

com_sh =df({
    '매출':[700, 600,500,400,300,200],
    '비용':[550,430,350,290,110,100]},index=['7월','8월','9월','10월','11월','12월'])
# print(com_sh)
com_sh['이익']=com_sh['매출']-com_sh['비용']
print(com_sh)

com_year=pd.concat([com_fh,com_sh])
print(com_year)
total=df(com_year.sum(),columns=['총 실적']).T
print(pd.concat([com_year,total]))


# 3. 다음 행렬과 같은 배열이 있다.
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
# -1.이 배열에서 3의 배수를 찾아라.
print(x%3==0)
# -2.이 배열에서 4로 나누면 1이 남는 수를 찾아라.
print(x%4==1)
# -3.이 배열에서 3으로 나누면 나누어지고 4로 나누면 1이 남는 수를 찾아라.
print((x%3==0)&(x%4==1))
