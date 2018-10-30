#빅데이터분석, 딥러닝, 머닝러신

#데이터->훈련데이터(70%)/테스트데이터(30%)->모델->테스트데이터입력->모델 평가->평가 결과에 따른 feedback

import random

# random.seed(999) #seed값을 주면 고정된 랜덤값을 뽑아낸다. 모델 평가시 동일한 값을 가지고 비교해보기 위해 필요.
# print(random.randrange(100))
# print(random.randrange(100))
# print(random.randrange(100))

# for _ in range(10):

# random.seed(999)
# a=[random.randrange(100) for _ in range(10)]
# print(a)
#
# print([i for i in range(10)])
# print([i for i in a])
# print([i for i in a if i%2])
# print([i for i in a if i%2][::-1])
# print([i for i in a [::-1] if i %2])
# print([i for i in reversed(a) if i%2])
#
# a1 = [random.randrange(100) for _ in range(10)]
# a2 = [random.randrange(100) for _ in range(10)]
# a3 = [random.randrange(100) for _ in range(10)]
# b=[a1,a2,a3]
# print(b)
# print(sum([1,3,5]))
#
# print([sum(i) for i in b])
# print(sum([sum(i) for i in b]))
# print([0 for i in b])
# print([0 for i in b for j in i])
# print([j for i in b for j in i])
#
# print([j for i in b for j in i if j%2])
# print([[j for j in i]for i in b])
# print([[j for j in i if j%2]for i in b])
#
# print("-"*50)
# print(b)
# print([i for i in b[::-1]])
# print([[j for j in i[::-1]]for i in b[::-1]])

# print(2**1000)
# print(str(2**1000))
# print(len(str(2**1000)))
#
# #2**1000에 들어가는 숫자들의 합을 구하시오.
# a="hello"
# for i in range(len(a)):
#     print(a[i])
#
# a=2**1000
# print(sum([int(i) for i in str(a)]))


