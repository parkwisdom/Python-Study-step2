import numpy as np

# a1=np.arange(24)
# a2=np.arange(24).reshape(4,6)
# a3=np.arange(24).reshape((2,3,4))
# a1[5]=1000
# a2[0,1]=1000
# a3[1,0,1]=1000 #2번째 행, 1번째 열, 2번째 depth(요소)
#
# print(a2)
#
# #a2에서 7~10,13~16을 추출하여 출력
# print(a2[1:3,1:5])
# print(a2[1:-1,1:-1])
#
# a2[:,1:3]=99
# print(a2)
#
# a1=np.arange(1,25).reshape(4,6)
# even_a=a1%2==0
# a1[even_a]

import pandas as pd

# rain=pd.read_csv("seattle.csv")
#
# rain_r=rain['PRCP']
# # print(rain_r) #Series 타입.
# rain_r=rain['PRCP'].values
# print(rain_r)
# print(type(rain_r)) #numpy.ndarray 타입
# print("데이터 크기:",len(rain_r))
#
# days_a=np.arange(0,365)
# con_jan=days_a<31 #True: 31, False:334
# print(con_jan[:40])
# print(rain_r[con_jan]) #1월달 강수량 데이터 참조
#
# print(np.sum(rain_r[con_jan]))#1월달 강수량의 총합
# print(np.mean(rain_r[con_jan])) #mean: 평균 , median: 중앙값


# a=np.arange(1,25).reshape((4,6)) # 팬시 인덱싱: 배열에 인데스 배열을 전달해서 데어터를 참조
# print(a)
#
# print([a[0,0],a[1,1],a[2,2],a[3,3]])
# print(a[[0,1,2,3],[0,1,2,3]])
#
# print(a[:,[1,2]])
#
# a=np.random.randint(1,10,(2,3))
# print(a)
# print(a.ravel()) #2차원->1차원 변경
#
# b=a.ravel()
# print(b)

# #배열 변경,삭제, 추가...
#     #resize: 배열크기 변경(요소 수 변경o), reshape: 배열 변경(요소 수 변경x)
# a=np.random.randint(1,10,(5,5))
# print(a)
# print(a.shape)
# a.resize(10,10)
# print(a)
#
# a=np.arange(1,10).reshape(3,3)
# b=np.arange(10,19).reshape(3,3)
# res=np.append(a,b) #1차원 배열(axis를 지정 안하면)
# print(res)
# print(a)
#
# print("-"*30)
# res=np.append(a,b,axis=0) # 행방향 2차원 배열
# print(res)
#
# print("-"*30)
# res=np.arange(10,20).reshape(2,5)
# print(res)
# # np.append(a,res,axis=0) # 기준 축과 shape 다르면 append시 오류 발생
#
# print("-"*30)
# res=np.append(a,b,axis=1) #열방향,2차원 배열
# print(res) #3*6
# #shape이 다르므로 오류, x=np.arange(10,20).reshape(2,5)
# # np.append(res,x,axis=1)
#

# print("-"*30)
#     #추가
# a=np.arange(1,10).reshape(3,3)
# # a=np.insert(a,1,99)
# # print(a)
# a=np.insert(a,2,99,axis=0) #행추가
# print(a)
# a=np.insert(a,2,99,axis=1)  #열추가
# print(a)
#
#     #삭제
# print("-"*30)
# a=np.arange(1,10).reshape(3,3)
# print(np.delete(a,1))
# #a배열의 1번 인덱스 행 제거
# a=np.delete(a,1,axis=0)
# print(a)
# #a배열의 2번 인덱스 열 제거
# a=np.delete(a,2,axis=1)
# print(a)

    #배열 간에 결합(concatenate,vstack,hstack)
print("-"*30)
a=np.arange(1,7).reshape(2,3)
print(a)
b=np.arange(7,13).reshape(2,3)
print(b)
res=np.concatenate((a,b))
print(res)

    #배열 쌓기 &나누기
print("-"*30)
a=np.arange(1,7).reshape(2,3)
b=np.arange(7,13).reshape(2,3)
print(np.vstack((a,b,a,b))) #수직방향으로 배열 쌓기
print(np.hstack((a,b))) #수평방향으로 배열 쌓기

a=np.arange(1,25).reshape(4,6)
res=np.hsplit(a,2) #좌우로 2개 그룹으로 나눔
print(res)

    #출력 타입 설정
print("-"*30)
x=np.array([1,2])
print(x.dtype)
x=np.array([1.,2.])
print(x.dtype)
x=np.array([1,2],dtype=np.int64)
print(x.dtype)

print("-"*30)
x=np.array([[1,2],[3,4]])
y=np.array([[5,6],[7,8]])
v=np.array([9,10])
w=np.array([11,12])
    #벡터의 내적
print(np.dot(v,w)) #9*11+10*12=219
print(v.dot(w))
    #행렬과 벡터의 곱
print(x.dot(v)) #[29 67] 1차원 배열
    #행렬 곱
print(np.dot(x,y))

x=np.array([[1,2],[3,4]])
print(x.T)  #전체행렬:대각선(1,1 /2,2...)을 기준으로 자리바꿈

print("-"*30)
x=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
v=np.array([1,0,1])
y=np.empty_like(x)
# print(y)

for i in range(4):
    y[i,:]=x[i,:]+v #[1,2,3]+[1,0,1]=[2,2,4]
print(y)

print("-"*30)
a=np.array([[1,2],[4,5]])
s=np.prod(a) #행렬 전체 수의 곱
s=np.prod(a,axis=0) #세로로 같은 줄 곱하기
s=np.prod(a,axis=1) #가로로 같은 줄 곱하기
print(s)

