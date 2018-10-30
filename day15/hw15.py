# 다음 배열은 첫번째 행(row)에 학번, 두번째 행에 영어 성적, 세번째 행에 수학 성적을 적은 배열이다.
# 영어 성적을 기준으로 각 열(column)을 재정렬하라.
import numpy as np
a=np.array([[  1,    2,    3,    4],
       [ 46,   99,  100,   71],
       [ 81,   59,   90,  100]])

arr=np.argsort(a[1],axis=0)
print(a[:,arr])

# 실수로 이루어진 5 x 6 형태의 데이터 행렬을 만들고 이 데이터에 대해 다음과 같은 값을 구한다.
x=np.arange(0,30).reshape(5,6)
print(x)
# 1.전체의 최댓값
print(np.max(x))
# 2.각 행의 합
print(np.sum(x,axis=1))
# 3.각 열의 평균
print(np.mean(x,axis=0,dtype=int))
