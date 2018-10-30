import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

a=np.arange(1,10).reshape(3,3)
print(a)
print(np.sum(a)) #axis=None
print(np.sum(a,axis=0))
print(np.sum(a,axis=1))

print("-"*50)
print(np.max(a))
print(np.max(a,axis=0))
print(np.max(a,axis=1))
#
# # cumsum() : 누적합계
# print(np.cumsum(a))
# print(np.cumsum(a,axis=0))
# print(np.cumsum(a,axis=1))
#
# median() : 중앙값
print(np.median(a))
print(np.median(a,axis=0))
print(np.median(a,axis=1))

# # a=np.arange(1,5).reshape(2,2)
# # print(np.median(a))
#
# # std() : 표준편차
# print(np.std(a))
# print(np.std(a,axis=0))
# print(np.std(a,axis=1))

a=np.arange(1,25).reshape(4,6)
b=np.arange(25,49).reshape(4,6)

print(a+b)
print(a+100)

new_arr=np.full_like(a,10)
print(a+new_arr) #==print(a+10)

a=np.arange(5).reshape(1,5)
print(a)

b=np.arange(5).reshape(5,1)
print(b)

print(a+b)

a=np.random.randint(0,9,(3,3))
print(a)

a1=np.copy(a)
a1[:,0]=99
print(a1)
print(a)

uns=np.random.random((3,3))
print(uns)
uns1=uns
uns2=uns
uns3=uns
print("="*50)
uns1.sort() # axis값 생략= 마지막 축이 기준(행,열),3차원(행,열,길이)
print(uns1)
uns1.sort(axis=1) #열을 기준으로
print(uns1)
uns1.sort(axis=-1) #마지막 축을 기준으로
print(uns1)

print('@@@')
a=np.array([40,30,10,20])
j=np.argsort(a) #오름차순으로 정렬했을 때 각 요소의 위치
print(j)
print(a[j])
print(np.sort(a))

# np.sort(a,axis=0)[ : :-1] #내림차순됨.

x=np.array([4,3,1,5,2,6,0])
# print(np.sort(x)) #정렬 결과만 사본으로 리턴
# print(x) #원 배열은 그대로
# x.sort() #배열 자체가 정렬
# print(x)

xrev=np.sort(x)[::-1] # 뒤에서부터 출력 내림차순
print(xrev)

x=np.array([14,13,11,15,12,16,10])
print(x[np.argsort(-x)]) #[5 3 0 1 4 2 6] 내림차순
print(np.argsort(x)) #[6 2 4 1 0 3 5]


arr=np.arange(0,2*3*4) #0~23(24개)
v=arr.reshape([2,3,4])#1차원 ->3차원 변환 : 행(row),열(col),깊이(depth)
print(v)

print(v.sum())
print(v.ndim)

res1=v.sum(axis=0) #2*3*4 =>3*4
print(res1.shape)
print(res1)

res2=v.sum(axis=1) #2*3*4 =>2*4
print(res2.shape)
print(res2)

res3=v.sum(axis=2) #2*3*4 =>2*3
print(res3.shape)
print(res3)