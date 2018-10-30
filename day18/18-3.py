import pandas as pd
from pandas import DataFrame,Series
import numpy as np
import json

# abalone=pd.read_csv('abalone.txt',sep=",",
#             names=['sex','length','diameter','height','whole_weight','shucked_weight','viscera_weight','shell_weight','rings'],
#             header=None)
# print(abalone)
# print(np.sum(pd.isnull(abalone))) # nan 의 갯수
#
# print(abalone.describe()) # count ,mean std  ,min, 25%,75%,max 에 대해 각각의 값을 한번에 구해줌 //==R:summary()
#
# grouped=abalone['whole_weight'].groupby(abalone['sex'])
# print(grouped)
# print(grouped.size()) #그룹 단위의 크기
# print(grouped.sum()) #그룹 단위 '전체 무게'의 합계
# print(grouped.mean()) #그룹 단위 '전체 무게'의 합계
#
# print(abalone.groupby(abalone['sex']).mean())  # 전체 열에 대해 성별로 구분하여 각각의 평균을 구함
# abalone['length_cat']=np.where(abalone.length>np.median(abalone.length),'length_long','length_short' )
# print(abalone[['length','length_cat']][:10])
#
# # sex length_cat
# # F   L_L : 평균값(whole_weight)
# #     L_S : 평균값
# print(abalone['whole_weight'].groupby(abalone['sex']).mean())
# print(abalone['whole_weight'].groupby([abalone['sex'],abalone['length_cat']]).mean())  #sex그룹화 ->길이 그룹화
#
# print(abalone.groupby(['sex','length_cat'])['whole_weight'].mean()) #sex그룹화 ->길이 그룹화
#
# #성별로 그룹화 한 다음. for문 사용하여 그룹 이름별로 데이터셋을 출력
# print('-'*40)
# for sex, group_data in abalone[['sex','length_cat','whole_weight','rings']].groupby('sex'):
#     print(sex)
#     print(group_data[:5])
#
# print('-'*40)
# for sex, group_data in abalone[['sex','length_cat','whole_weight','rings']].groupby(['sex','length_cat']):
#     print(sex)
#     print(group_data[:5])
#
#
# df=DataFrame([[1.4,np.nan],
#               [7.1,-4.5],
#               [np.nan, np.nan],
#               [0.75,-1.3]],
#              index=['a','b','c','d'],
#              columns=['one','two'])
# print(df)
# print(df.sum(axis=0))
# print(df.mean(axis=1,skipna=False))
# print('-'*40)
# print(df)
# print(df.idxmax())
#
# print('-'*40)
#
db=json.load(open('database.json'))
print(len(db))

# {키:{키:밸류,키:밸류},키:밸류.....} 몹시 복잡! 이럴 땐 첫번째 요소들만 추출해서 확인해보는 방법.
print('-'*40)
print(db[0].keys())
print('-'*40)
print(db[0]['nutrients'])
print('-'*40)
print(db[0]['nutrients'][0])
print('-'*40)
print(db[0]['nutrients'][0]['value'])

print('-'*40)
nutrients=DataFrame(db[0]['nutrients']) #[162 rows x 4 columns]
print(nutrients[:7])
print('-'*40)
info_keys=['description', 'group', 'id','manufacturer']
info=DataFrame(db,columns=info_keys) # info에 저장된건 데이터프레임.
# print(info[:5])
print(info['group'])
print('-'*40)

# print(info.info())

#     대한민국(object; 계층구조에서 제일 꼭대기층)
# 출생시도:서울,경기,강원...제주

print(pd.value_counts(info.group)) #'group'이라는 컬럼에 있는 목록각각이 몇개인지 ./.
print('-'*40)

nutrients=[]
for rec in db:
    fnuts=DataFrame(rec['nutrients'])
    fnuts['id']=rec['id']
    nutrients.append(fnuts)
# print(nutrients)
print(nutrients.duplicated().sum())
nutrients=nutrients.drop_duplicates()
print(nutrients)