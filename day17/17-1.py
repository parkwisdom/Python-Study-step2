import pandas as pd
from pandas import DataFrame as df
    #index무시 : ignor_index

# df_5=df({
#     'a':['a0','a1','a2'],
#     'b': ['b0', 'b1', 'b2'],
#     'c': ['c0', 'c1', 'c2'],
#     'd': ['d0', 'd1', 'd2']},index=['r0','r1','r2'])
#
# df_6=df({
#     'a':['a3','a4','a5'],
#     'b': ['b3', 'b4', 'b5'],
#     'c': ['c3', 'c4', 'c5'],
#     'd': ['d3', 'd4', 'd5']},index=['r3','r4','r5'])
#     # index무시 : ignor_index
# df_56_with_index =pd.concat([df_5,df_6])
# print(df_56_with_index)
#
# df_56_with_index =pd.concat([df_5,df_6],ignore_index=False) #ignore_index =False인덱스 설정값인식
# print(df_56_with_index)
#
# df_56_with_index =pd.concat([df_5,df_6],ignore_index=True) #ignore_index=True인덱스 설정값 무시
# print(df_56_with_index)
#
# print('-'*40)
#     #keys : 계층구조를 나타내기 위해 사용
# df_56_with_index =pd.concat([df_5,df_6],ignore_index=False,keys=['df5','df6'], names=['df_name','num_name'])
# print(df_56_with_index)
#
# # print(df_56_with_index.ix['df5'][0:2]) #계층구조로 나누면 워하는 그룹만 출력가능>오류 뜨는 이유 ix때문..더좋은기능있으니 일단 넘어감.
#
# df_7=df({
#     'a':['a0','a1','a2'],
#     'b': ['b0', 'b1', 'b2'],
#     'c': ['c0', 'c1', 'c2'],
#     'd': ['d0', 'd1', 'd2']},index=['r0','r1','r2'])
#
# df_8=df({
#     'a':['a3','a4','a5'],
#     'b': ['b3', 'b4', 'b5'],
#     'c': ['c3', 'c4', 'c5'],
#     'd': ['d3', 'd4', 'd5']},index=['r2','r3','r4'])
#
# df_78=pd.concat([df_7,df_8],verify_integrity=False) #verify_integrity : index값 겹칠 경우 합치지 않고 다 출력
# print(df_78)

# print('-'*40) # 위쪽은 데이터프레임 합치기//아래쪽은 데티러프레임+시리즈 합치기.
#
# df_1=df({
#     'a':['a0','a1','a2'],
#     'b': ['b0', 'b1', 'b2'],
#     'c': ['c0', 'c1', 'c2'],
#     'd': ['d0', 'd1', 'd2']},index=[0,1,2])
#
Series_1=pd.Series(['S1','S2','S3'],name='S')
print(Series_1)
#
# print(pd.concat([df_1,Series_1]))
# print('-'*40)
# print(pd.concat([df_1,Series_1],axis=1,ignore_index=True))
#
# #Series끼리 합치기
# Series_1=pd.Series(['S1','S2','S3'],name='S')
# Series_2=pd.Series([0,1,2])
# Series_3=pd.Series([3,4,5])
# print(pd.concat([Series_1,Series_2,Series_3],axis=1))
# print(pd.concat([Series_1,Series_2,Series_3],axis=1,keys=['C0','C1','C2']))
#
# print('-'*40)
# df_1=df({
#     'a':['a0','a1','a2'],
#     'b': ['b0', 'b1', 'b2'],
#     'c': ['c0', 'c1', 'c2'],
#     'd': ['d0', 'd1', 'd2']},index=[0,1,2])
# Series_4=pd.Series(['S1','S2','S3','S4'],index=['a','b','c','e'])
# print(Series_4)
# print(df_1.append(Series_4,ignore_index=True))
#
# #DataFrame Join/Merge. 데이터 병합
#
# df_left=df({
#     'KEY':['a0','a1','a2','a3'],
#     'b': ['b0', 'b1', 'b2','b3'],
#     'c': ['c0', 'c1', 'c2','c3']})
#
# df_right=df({
#     'KEY':['a2','a3','a4','a5'],
#     'd': ['d0', 'd1', 'd2','d3'],
#     'e': ['e0', 'e1', 'e2','e3']})
#
# print(df_left)
# print(df_right)
#
#
# df_merge_how_left=pd.merge(df_left,df_right) #key값이 같은 값들끼리 병합
# print(df_merge_how_left)
#
# df_merge_how_left=pd.merge(df_left,df_right,how='left')
# print(df_merge_how_left)
#
# df_merge_how_left=pd.merge(df_left,df_right,how='left',on='KEY')
# print(df_merge_how_left)
#
# df_merge_how_left=pd.merge(df_left,df_right,how='right',on='KEY')
# print(df_merge_how_left)
#
# df_merge_how_inner=pd.merge(df_left,df_right,how='inner',on='KEY')
# print(df_merge_how_inner)
#
# df_merge_how_outer=pd.merge(df_left,df_right,how='outer',on='KEY', indicator=True) #indicator=True어느쪽 프레임에 값이 있는지 표현
# print(df_merge_how_outer)
#
# print('-'*40)
# df_left_2=df({
#     'KEY':['a0','a1','a2','a3'],
#     'a': ['b0', 'b1', 'b2','b3'],
#     'b': ['b0', 'b1', 'b2','b3'],
#     'c': ['c0', 'c1', 'c2','c3']})
#
# df_right_2=df({
#     'KEY':['a2','a3','a4','a5'],
#     'b': ['b0', 'b1', 'b2','b3'],
#     'd': ['d0', 'd1', 'd2','d3'],
#     'e': ['e0', 'e1', 'e2','e3']})
# print(pd.merge(df_left_2,df_right_2,how='inner',on='KEY',suffixes=('_left','_right')))

print('-'*40)
df_left=df({
    'a': ['a0', 'a1', 'a2','a3'],
    'b': ['b0', 'b1', 'b2','b3']}, index=['k0','k1','k2','k3'])

df_right=df({
    'c': ['c0', 'c1', 'c2','c3'],
    'd': ['d0', 'd1', 'd2','d3']},index=['k2', 'k3', 'k4','k5'])

#index기준으로 데이터프레임 합시는 작업: pd.merge(),join()
print(pd.merge(df_left,df_right,left_index=True,right_index=True,how='left'))
print(df_left.join(df_right,how='left'))
print('-'*40)
print(pd.merge(df_left,df_right,left_index=True,right_index=True,how='right'))
print(df_left.join(df_right,how='right'))
print('-'*40)
print(pd.merge(df_left,df_right,left_index=True,right_index=True,how='outer'))
print(df_left.join(df_right,how='outer'))
print('-'*40)
print(pd.merge(df_left,df_right,left_index=True,right_index=True,how='inner'))
print(df_left.join(df_right,how='inner'))

