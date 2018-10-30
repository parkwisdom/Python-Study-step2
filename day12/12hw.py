#1번 문제 힌트
# s='707'
# print(s.count('7'))

#1) 1~100000 사이에 있는 7의 개수를 세어보세여.
b=[i for i in str([i+1 for i in range(100000)])]
print(b.count(('7')))

#2) maria={'kor':94,'eng':91,'math':89,'sci':83}
#maria 딕셔너리에 저장된 점수의 평균을 출력하세요
maria={'kor':94,'eng':91,'math':89,'sci':83}
print(sum(maria.values())/len(maria))

# ★★★★★★★★★★★★★★★★★★★★★3번 어려움 다시보기
#3) 어떤 자연수 n이 있을 때, d(n)을 n의 각 자릿수
#숫자들과 n 자신을 더한 숫자라고 정의하자.
#예를 들어 d(91) = 9 + 1 + 91 = 101
#이 때, n을 d(n)의 제네레이터라고 한다.
#91은 101의 제네레이터이다.
#어떤 숫자들은 하나 이상의 제네레이터를 가지고 있는데,
#101의 제네레이터는 91 뿐 아니라 100도 있다. 그런데
#반대로, 제네레이터가 없는 숫자들도 있으며, 이런 숫자를
#셀프 넘버(self-number)라 한다. 예를 들어 1,3,5,7,
#9,20,31 은 셀프 넘버들이다.1 이상이고 5000 보다
#작은 모든 셀프 넘버들의 합을 구하라.

list=[]
for i in range(1,5000):
    a= i + sum([int(j) for j in str(i)])
    b=list.append(a)
print(sum(set(range(1,5000))-set(list)))




    # for y in range(1,50):
    #     [dn,y].append(str(y))
# print([[y for y in str(x)] for x in range(1,50)])
    # print(y)

    # print(y)
    # print(set(str(y)))


#3번문제 힌트
# i=567
# for t in str(i):
#     # print(t)
#     print(int(t)+1)

# print(set(range(1,5)))
# print(set(range(1,5))-set(range(1,3)))#{1,2,3,4}-{1,2}={3,4}