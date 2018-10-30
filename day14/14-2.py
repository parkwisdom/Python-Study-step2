import numpy as np
import matplotlib.pyplot as plt
a=np.array([[1,2,3],[4,5,6]])
b=np.ones_like(a)
print(b)

# 데이터 생성 함수

# 0~1 범위 내에서 균등 간격으로 5개의 수를 생성

a=np.linspace(0,1,5) #0-1까지 5개
print(a)
plt.plot(a,'o') #점으로 찍히는 그래프
plt.show()

a=np.arange(0,10,2, np.float) #0-10까지 2간격으로 float 형태로 출력
print(a)
print(type(a))
plt.plot(a,'s')
plt.show()

mean=0
std=1
a=np.random.normal(mean, std, 10000) #normal: 정규분포 그래프
print(a)
plt.hist(a,bins=100) #히스토그램 그래프 bins=100 구간의 수
plt.show()

a=np.random.rand(10000) #균등분포 (0~1)
plt.hist(a, bins=10)
plt.show()

a=np.random.randint(-100,100,size=10000)
print(a)
plt.hist(a,bins=10)
plt.show()

a=np.random.randint(0,10,(2,3))
print(a)
b=np.random.randint(0,10,(2,3))
print(b)

np.save("myarr1",a) #myarr1.npy-->save(): 배열을 바이너리 형태로 저장
np.savez("myarr2",a,b)
print("myarr1=", np.load("myarr1.npy"))
print("myarr2=", np.load("myarr2.npy"))

npzfiles = np.load("myarr2.npz")
print(npzfiles.files)
print(npzfiles['arr_0'])
print(npzfiles['arr_1'])

print(np.loadtxt("simple.csv",dtype=np.int)) #dtype: 내가 원하는 타입으로 정보 불러오기

data= np.loadtxt("height.csv",delimiter=",",skiprows=1,
                 dtype={'names':("order","name","height(cm)"),'formats':('i','S20','i')})
print(data)

#savetxt함수: 배열을 텍스트 파일로 저장
data= np.random.random((3,4))
print(data)
np.savetxt("saved.csv",data,delimiter=",")
print(np.loadtxt("saved.csv",delimiter=","))

arr=np.random.random((5,2,3))
print(type(arr))
print(arr.shape)
print(len(arr))
print(arr.ndim)
print(arr.size)
print(arr)
print(arr.dtype)
print(arr.astype(np.int)) #원래 타입을 int타입으로 변경
print(arr.dtype)
print(arr)
arr=arr.astype(np.float)
print(arr)

print(np.info(np.ndarray.dtype))

a=np.arange(1,10).reshape(3,3)
# print(a)
b=np.arange(9,0,-1).reshape(3,3) #감소의 경우 감소폭 써줘야함
# print(b)
print(np.dot(a,b))

print("="*30)
print(a-b)
print(np.subtract(a,b))

print("="*30)
print(a+b)
print(np.add(a,b))

print("="*30)
print(a/b)
print(np.divide(a,b))

print("="*30)
print(a*b)
print(np.multiply(a,b))

print("="*30)
print(b)
print(np.exp(b)) #2.71832323e+00=2.718...(자연상수)

print(a)
print(np.sqrt(a))
print(np.sin(a)) #sin함수
print(np.cos(a)) #cos함수
print(np.tan(a)) #tan함수
print(np.log(a)) #log함수

print(a)
print(b)
print(np.dot(a,b))

print(a==b)
print(np.array_equal(a,b))

print(a.sum()) #axis
print(np.sum(a))
print("="*30)
print(a)
print(a.sum(axis=0)) #axis=0, 행을 기준으로 각 행의 동일한 인덱스 요소를 그룹화해라.
print(a.sum(axis=1)) #axis=1, 열을 기준으로 각 열의 동일한 인덱스 요소를 그룹화해라.

