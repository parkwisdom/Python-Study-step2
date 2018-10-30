import numpy as np
# print(np.__version__)
#
# list1=[1,2,3,4]
# print("list=",list1)
# a=np.array(list1)
# print("array=",a)
# print(a.shape) #shape: (4,)-->rank: 1
# b=np.array([[1,2,3],[4,5,6]]) #rank: 2
# print(b)
# print(b.shape) #shape: (2,3)
# print(b[0,0])
# print(type(b))
# print(a[2])
#
# #벡터화 연산
# #개념: 배열의 각 요소에 대한 반복 연산을 하나의 명령으로 처리
#
# #벡터화 연산을 하지 않은 일반적인 반복문 연산(속도 느림)
data=[1,2,3,4,5]
ans=[]
for i in data:
    ans.append(2*i)
print(ans)

#벡터화 연산 (for 반복문이 없음 )->속도 무척 빠름
x=np.array(data)
print(2*x) #x = array 데이터를 두배해라
print(2*data) #data = list..데이터를 두번 반복해라
#
a=np.array([1,2,3])
b=np.array([10,20,30])
print(a*2+b)
print(a==2)
print(b>10)
print((a==2)&(b>10))
print(a.shape) #shape
print(a.ndim) #rank
print(a.dtype)
#
# a=np.zeros(4)
# print(a) #[0. 0. 0. 0.]
# print(type(a)) #자료구조? <class 'numpy.ndarray'>
# print(a.dtype) #자료형?(자료구조에 들어가 있는 형태의 타입) float64
#
# a=np.zeros((2,2)) #0으로 초기화시 사용
# print(a)
# a=np.ones((2,3)) #1로 초기화시 사용
# print(a)
# a=np.full((2,3),5) #5로 채워라.
# print(a)
# a=np.eye(5) #5행 5열의 단위행렬(항등원)
# print(a)
#
# c=np.array(range(20)).reshape((4,5)) #1차원 (20,)--> 2차원(4,5)변경
# print(len(c)) #행의 개수
# print(len(c[0])) #0번(첫번째)열의 길이 = 0번 열에 있는 요소(값) 개수
# print(c.ndim) #rank: 2차원
# print(c.shape) #shape:(4,5)
#
# print(c)
# print(c>10)
# print(c[c>10])
#
# c[c>10]=99
# print(c)

# arr=np.arange(0, 3*2*4)
# print(arr)
# print(len(arr))
# v=arr.reshape([3,2,4]) #2행 4열 행열이 3개로 나눠짐
# print(v)
# print(len(v)) #[ [[[],[]], [[],[]], [[][]] ] 큰 대괄호 안에 3묶음의 요소
# print(len(v[0])) #[ [[[],[]], [[],[]], [[][]] ] 3묶음의 요소 안에 또 두개씩의 요소
# print(len(v[0][0])) #[ [[[],[]], [[],[]], [[][]] ] 가장 안쪽 대괄호에 4개의 요소 들어있음
#
# a=np.arange(0,3*4)
# a=a.reshape([3,4])
# print(a)
#
# b=np.array([0,1,2,3,4])
# print(b[2])
# print(b[-1])
#
# #다차원 배열을 슬라이싱 할 때 사용되는 콤마(,)로 차원을 구분(축)
# print(a) #(3,4)
# print(a[0,1])
# print(a[-1,-1])
#
# print(a[0, : ])
#
# #두번째 열 전체를 추출
# print(a[:,1])
# #두번째 행의 두번째 열부터 끝까지 추출
# print(a[1, 1: ])
# #(2,2) 행열 만들기
# print(a[:2,:2])
#
# #인덱싱: 행 지정, 슬라이싱: 추출 열 지정
# print(a[1,:]) #rank: 1차원
# print(a[1,:].shape) #(4,)
#
# print(a[1:2, :]) #rank: 2차원
# print(a[1:2, :].shape) #(1, 4)
#
# a=np.array([[1,2],[3,4],[5,6]])
# print(a.shape)
# print(a)
# print(a[[0,1,2],[0,1,0]]) # 0-0,1-1,2-0==> [1 4 5]==>array (벡터)
# print(a[0,0],a[1,1],a[2,0]) #1 4 5 ==>스칼라값
# print([a[0,0],a[1,1],a[2,0]]) #[1, 4, 5]==>list
# print(np.array([a[0,0],a[1,1],a[2,0]])) #[1 4 5]==>array.
#
# a=np.array([[1,2],[3,4],[5,6]])
# print(type(a[0,0])) #int32 ->스칼라
# s=a[[0,1],[1,1]]
# print(s)

#부울린 값 참조
lst=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
x=np.array(lst)

bool_ind_arr=np.array([
    [False,True,False],
    [True,False,True],
    [False,True,False]
])

print(type(lst))
print(type(bool_ind_arr))

res=x[bool_ind_arr]
print(res)

lst=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
x=np.array(lst)
bool_ind=(x%2==0) #산수연산 ->비교연산 ->논리연산
print(bool_ind)
print(x[bool_ind])

print(x[x%2 == 0])
