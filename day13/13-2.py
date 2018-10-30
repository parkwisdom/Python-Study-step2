#결측치 처리 연습 & 데이터프레임 사용

from pandas import DataFrame,Series
import pandas as pd

# pd.DataFrame()
import numpy as np
# print(np.random.randn(5,3)) #표준정규분포, 평균(기댓값):0, 표준편자 :1
df=pd.DataFrame(np.random.randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])
# print(df)
# print(type(df))
# print(type(df['W']))

# print(df.drop('E')) # E가 빠진 형태로 출력이 될뿐이지 실제로 빠지지 않음
# df=df.drop('E') #E가 제거되어 df 대입된 형태
# print(df)

# print(df.shape)
# print(df.loc['A'])
# print(df.iloc[0])
# print(df.loc[['A','B'],['X','Y']])


d={'A':[1,2,np.nan],'B':[5,np.nan,np.nan],'C':[1,2,3]}
# print(d)
df=pd.DataFrame(d)
# print(df)
# print(type(df))

# print(df.dropna()) #nan값이 있는 행값삭제
# print(df.dropna(axis=0)) #nan값이 있는 행값삭제
# print(df.dropna(axis=1)) #nan값이 있는 열값삭제

# print(df.dropna(thresh=2))
# print(df.dropna())
#
# print(df['A'].fillna(value="imsi"))
# print(df.fillna(value='imsi'))

print(df)
#A열에 대해서 na값을 A열의 평균으로 대체
#print(df['A'].mean())
print(df['A'].fillna(value=df['A'].mean()))