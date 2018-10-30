# 연속형 변수 ->이산화(2개 이상의 범주로 변환)
import numpy as np
import pandas as pd
from pandas import DataFrame
np.random.seed(777)

df=DataFrame({'c1':np.random.randn(20),
           'c2':['a','a','a','a','a','a','a','a','a','a',
                 'b','b','b','b','b','b','b','b','b','b']})
print(df)

#c1을 최소값~최대값 구간을 10개로 균등하게 분할
bins=np.linspace(df.c1.min(), df.c1.max(), 10)
df['c1_bin']=np.digitize(df['c1'],bins) #c1을 bins의 나누어진 간격에 따라 숫자로 표현?
print(df)

print(df.groupby('c1_bin')['c1'].size())
print(df.groupby('c1_bin')['c1'].mean())
print(df.groupby('c1_bin')['c1'].std())
print(df.groupby('c1_bin')['c2'].value_counts())
# print(df[df['c1_bin']==2]) # c1_bin에서 값을 2를 가지는 것을 추출?

print('-'*40)

print(df)
print(pd.get_dummies(df['c1_bin'],prefix='c1')) #각각의 난수 데이터가 어디col에 속하는지 확인하는

print(df.c1.mean())
df['high_low']=np.where(df['c1']>=df.c1.mean(),'high','low')  #c1 값이 c1의 평균값보다 크거나 같으면 high, 작으면 low
print(df)

print(df.groupby('high_low')['c1'].size())
print(df.groupby('high_low')['c1'].mean())
print(df.groupby('high_low')['c1'].std())

Q1=np.percentile(df['c1'],25) #25%위치 =Q1
Q3=np.percentile(df['c1'],75) #75%위치 =Q3
# print(Q1,Q3)

#<25, 25< <75, 75<
df['h_m_l']=np.where(df['c1']>=Q3,'01_high',np.where(df['c1']>=Q1,'02_medium','03_low')) #컬럼을 여러개의 범주로 나누는 방법!
print(df)

print(df.groupby('h_m_l')['c1'].size())
print(df.groupby('h_m_l')['c1'].mean())
print(df.groupby('h_m_l')['c1'].std())

#데이터 재구조화 (reshaping):pivot,stack, melt 함수 등

data=DataFrame({'cust_id': ['c1', 'c1', 'c1', 'c2', 'c2', 'c2', 'c3', 'c3', 'c3'],
'prod_cd': ['p1', 'p2', 'p3', 'p1', 'p2', 'p3', 'p1', 'p2', 'p3'],
'grade' : ['A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'B'],
'pch_amt': [30, 10, 0, 40, 15, 30, 0, 0, 10]})
print(data)
#행-고객 id / 열 - 상품코드 / 데이터-구매금액
#     p1  p2  p3
# c1  30  10  0
# c2....
# c3

dp=data.pivot(index='cust_id',columns='prod_cd',values='pch_amt')
print(dp)

dp=pd.pivot_table(data,index='cust_id',columns='prod_cd',values='pch_amt')
print(dp)

#index값을 2개 이상 줄 때 pivot 에서는 안되지만 ,pivot_table에서는 가능
dp=pd.pivot_table(data,index=['cust_id','grade'],columns='prod_cd',values='pch_amt')
print(dp)

dp=pd.pivot_table(data,index='cust_id',columns=['grade','prod_cd'],values='pch_amt')
print(dp)
print('-'*40)

mul_index=pd.MultiIndex.from_tuples(
    [('cust_1','2018'),
    ('cust_1', '2019'),
    ('cust_2', '2018'),
    ('cust_2', '2019')])
print(mul_index)

data=DataFrame(data=np.arange(16).reshape(4,4),
          index=mul_index, columns=['prd_1','prd_2','prd_3','prd_4'],dtype=int)
print(data)
#위내용을 아래와 같으 쌓고 싶을때 : stack()함수 사용.
# cust_1  2018  prd_1     0
#               prd_2     1
#               prd_3     2
#               prd_4     3
#         2019  prd_1     4
#               prd_2     5
#               prd_3     6
#               prd_4     7
# cust_2  2018  prd_1     8
#               prd_2     9
data_stacked=data.stack()
print(data_stacked)
print(data_stacked.index)
print(data_stacked['cust_2']['2018'][['prd_1','prd_2']])

data.ix['cust_2','prd_4']=np.nan
print(data)
print(data.stack())
print(data.stack(dropna=False))

print('-'*40)
print(data_stacked)
print('-'*40)
print(data_stacked.unstack()) # unstack : stack 을 원래대로 돌리는 기능
print('-'*40)
print(data_stacked.unstack(level=-1)) #default: level=-1
print('-'*40)
print(data_stacked.unstack(level=0)) #level=0 : 다른 변수로 정렬
print('-'*40)
print(data_stacked.unstack(level=1))

print('-'*40)
data_stacked_unstacked=data_stacked.unstack(level=-1)
print(data_stacked_unstacked)
print(type(data_stacked_unstacked)) #DataFrame

#reset_index : 인덱스를 컬럼으로..
dsu_df=data_stacked_unstacked.reset_index()
print(dsu_df)

dsu_df=dsu_df.rename(columns={'level_0':'custID','level_1':'year'}) # 행열 이름 바꾸기.
print(dsu_df)

data=DataFrame({'cust_id': ['c1', 'c1', 'c2', 'c2'],
'prod_cd': ['p1', 'p2', 'p1', 'p2'],
'pch_cnt' : [1,2,3,4],
'pch_amt': [100,200,300,400]})
print(data)
print('-'*40)
print(pd.melt(data))
print(pd.melt(data,id_vars=['cust_id','prod_cd'],var_name='pch_cd',value_name='pch_value'))
print('-'*40)
print(data)
data_melt=pd.melt(data,id_vars=['cust_id','prod_cd'],var_name='pch_cd',value_name='pch_value')
print(data_melt)
print(data_melt.index)
print(data_melt.columns)

data_melt_pivot=pd.pivot_table(data_melt,index=['cust_id','prod_cd'],columns='pch_cd',values='pch_value')
print(data_melt_pivot)
print(data_melt_pivot.index)
print(data_melt_pivot.columns)