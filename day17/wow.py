import pandas as pd
from pandas import DataFrame as df

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
#
# df_56_with_index = pd.concat([df_5,df_6])
# print(df_56_with_index)
#
# df_56_with_index=pd.concat([df_5,df_6],ignore_index=False)
# print(df_56_with_index)
#
# df_56_with_index=pd.concat([df_5,df_6],ignore_index=True)
# print(df_56_with_index)
#
# df_56_with_index=pd.concat([df_5,df_6],ignore_index=False,keys=['df5','df6'],names=['df_name','df_num'])
# print(df_56_with_index)
#
# print(df_56_with_index.ix['df5'][0:2])
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
# df_78=pd.concat([df_7,df_8],verify_integrity=False)
# print(df_78)
#
# df_1=df({
#     'a':['a0','a1','a2'],
#     'b': ['b0', 'b1', 'b2'],
#     'c': ['c0', 'c1', 'c2'],
#     'd': ['d0', 'd1', 'd2']},index=[0,1,2])
#
# Series_1=pd.Series(['S1','S2','S3'],name='S')
# print(Series_1)
#
# print(pd.concat([df_1,Series_1]))
# print(pd.concat([df_1,Series_1],axis=1,ignore_index=False))
#
# Series_1=pd.Series(['S1','S2','S3'],name='S')
# Series_2=pd.Series([0,1,2])
# Series_3=pd.Series([3,4,5])
# print(pd.concat([Series_1,Series_2,Series_3],axis=1))
# print(pd.concat([Series_1,Series_2,Series_3],axis=1,keys=['c0','c1','c2']))
#
# df_1=df({
#     'a':['a0','a1','a2'],
#     'b': ['b0', 'b1', 'b2'],
#     'c': ['c0', 'c1', 'c2'],
#     'd': ['d0', 'd1', 'd2']},index=[0,1,2])
# Series_4=pd.Series(['S1','S2','S3','S4'],index=['a','b','c','e'])
#
# print(df_1.append(Series_4,ignore_index=True))
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
# df_merge_how_left=pd.merge(df_left,df_right)
# print(df_merge_how_left)
#
# df_merge_how_left=df.merge(df_left,df_right,how='left')
# print(df_merge_how_left)
#
# df_merge_how_left=pd.merge(df_left,df_right,how='left',on='KEY')
# print(df_merge_how_left)
#
# df_merge_how_left=pd.merge(df_left,df_right,how='right',on='KEY')
# print(df_merge_how_left)
#
# df_merge_how_left=pd.merge(df_left,df_right,how='inner',on='KEY')
# print(df_merge_how_left)
#
# df_merge_how_left=pd.merge(df_left,df_right,how='outer',on='KEY',indicator=True)
# print(df_merge_how_left)
#
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
# print(pd.merge(df_left_2,df_right_2,how='inner'))
# print(pd.merge(df_left_2,df_right_2,how='inner',suffixes=('_left','_right')))
#
# df_left=df({
#     'a': ['a0', 'a1', 'a2','a3'],
#     'b': ['b0', 'b1', 'b2','b3']}, index=['k0','k1','k2','k3'])
#
# df_right=df({
#     'c': ['c0', 'c1', 'c2','c3'],
#     'd': ['d0', 'd1', 'd2','d3']},index=['k2', 'k3', 'k4','k5'])
#
# print(pd.merge(df_left,df_right,left_index=True,right_index=True,how='left'))
# print(df_left.join(df_right,how='left'))
#
# print(pd.merge(df_left,df_right,left_index=True,right_index=True,how='right'))
# print(df_left.join(df_right,how='right'))

df_left=df({
    'a': ['a0', 'a1', 'a2','a3'],
    'b': [0.5,2.2,3.6,0.4],
    'key':['k0','k1','k2','k3']})

df_right=df({
    'c': ['c0', 'c1', 'c2','c3'],
    'd': ['d0', 'd1', 'd2','d3'],
    'key':['k2', 'k3', 'k4','k5']})

df_all=pd.merge(df_left,df_right,how='outer',on='key')
print(df_all)

print(df.isnull(df_all))
print(df_all.isnull())

print(pd.notnull(df_all))
print(df_all.notnull())

print(df_all)
df_all.ix[[0,1],['a','b']]=None
print(df_all)

print(df_all[['a','b']].isnull())

print(df_all.isnull().sum())

print(df_all['a'].isnull().sum())

print(df_all.notnull().sum())

print(df_all.isnull().sum(1))

df_all['Nan_cnt']=df_all.isnull().sum(1)
df_all['NotNull_cnt']=df_all.notnull().sum(1)
print(df_all)

