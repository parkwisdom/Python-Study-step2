import pandas as pd
from pandas import DataFrame as df
import numpy as np

    #파일 읽어오기
# csv_test=pd.read_csv("test_csv_file.csv")
# print(csv_test)
# print(csv_test.shape)
#
# text_test=pd.read_csv("test_text_file.txt",sep="|")
# print(text_test)
#
# text_test=pd.read_csv("test_text_file.txt",sep="|",index_col=0)
# print(text_test)
# text_test=pd.read_csv("test_text_file.txt",sep="|",index_col="ID")
# print(text_test)
# print('-'*30)
# text_without_test=pd.read_csv("text_without_column_name.txt",sep="|",header=None, names=['ID','A','B','C','D'],index_col='ID')
# print(text_without_test)
#
#     #분석결과 파일로 저장하기
# data ={
#     'id':['a1','a2','a3','a4','a5'],
#     'x1': [1,2,3,4,5],
#     'x2': [3.0, 4.5, 3.2, 4.0, 3.5]
# }
# # data_df=DataFrame(data) #행번호가 함께 생성됨
# # print(data_df)
#
# data_df=df(data,index=['a1','a2','a3','a4','a5'])
# print(data_df)
#
# data_df_2=data_df.reindex(['a1','a2','a3','a4','a5','a6'])
# print(data_df_2)

# data_df_2.to_csv("data_df_2.csv",sep=",", na_rep='NaN')

# df_1=df(data=np.arange(12).reshape(3,4), index=['r0','r1','r2'], dtype='int',columns=['c0','c1','c2','c3'])
#
# print(df_1)
# print(df_1.T)
#
# print(df_1.axes)
# print(df_1.dtypes)
# print(df_1.size)
#
# print(type(df_1))
#
# print(df_1.values)
# print(type(df_1.values))
#
# df_2=df({'class_1':['a','a','b','b','c'],
#          'var_1':np.arange(5),
#          'var_2':np.random.randn(5)},
#         index=['r0','r1','r2','r3','r4'])
# print(df_2)
#
# print(df_2.index) #행범위 참조
# print(df_2.ix[2:]) #2번행부터 값만 출력
#
# print(df_2)
# print(df_2.head(3))
# print(df_2.tail(3))
#
# print(df_2.columns)
# print(df_2['class_1'])
#
# #class_1과 var_2 컬럼 출력
# print(df_2[['class_1','var_2']])
#
#
# idx=['r0','r1','r2','r3','r4']
# df_1=df({'c1':np.arange(5),
#          'c2':np.random.randn(5)},
#         index=idx)
# print(df_1)
#
# new_idx=['r0','r1','r2','r5','r6']
# # df_1=df_1.reindex(new_idx)
# # print(df_1)
#
# # df_1=df_1.reindex(new_idx,fill_value=0)
# # print(df_1)
#
# # df_1=df_1.reindex(new_idx,fill_value='missing')
# # print(df_1)
#
# df_1=df_1.reindex(new_idx,fill_value='NA')
# print(df_1)

    #시계열 데이터
# print(pd.date_range("2018-9-10","2018-12-31",freq='MS'))

date_idx= pd.date_range("09/10/2018", periods=10, freq='D')
print(date_idx)

df_2=df({"c1":[10,20,30,40,50,10,20,30,40,50]},index=date_idx)
print(df_2)
print('-'*30)

date_idx2= pd.date_range("09/05/2018",periods=20,freq='D')
print(date_idx2)
# df_2=df_2.reindex(date_idx2) #2018.9.10~9.19일
# print(df_2)
print('-'*30)

df_2=df_2.reindex(date_idx2,method='ffill')
print(df_2)
print('-'*30)
df_2=df_2.reindex(date_idx2,method='bfill')
print(df_2)
 #ffill 과 bfill의 차이