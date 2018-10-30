# a=[1,3,5,7,9,0,2,4,6,8]
#
# print(a[len(a)-1:0:-1])
# print(a[::-1])
# print(a[len(a)-1::-1])
#
# print(a[::-2])
# print(a[-2::-2])

#---------------------------

# def read_car():
#     f=open('car.csv','r')
#     rows=[]
#     for row in f:
#         # print(row)
#         print(row.strip().split(','))
# mycar=read_car()

# import csv
#
# def read_car():
#     f=open('../../Data/cars.csv','r')
#     rows=[]
#     for row in f:
#         # print(row)
#         rows.append(row.strip().split(','))
#     f.close()
#     return rows
#
#
# def write_car(rows):
#     f=open('../../Data/car_w.txt','w',newline='')
#     writer=csv.writer(f,delimiter=':')
#     for row in rows:
#         writer.writerow(row)
#     f.close()
#
# mycar=read_car()
# write_car(mycar)

##-------------------------------------------------

import numpy as np
# a=np.array([1,3,5])
# print(a)
# print(type(a))
#
#
# b=np.arange(7)
# print(b)
#
# c=np.arange(3,7,0.1)
# print(c)
#
# print(b)
# b+=1
# print(b)
#
# print(b<4)
# print(b[b<4])
#
# d=np.arange(15).reshape(3,5)
# print(d)
# print(d.shape)
# print(d+1)
# print(d[d>5])
# print("="*50)
# print(d[0])#행의 인덱스 출력
# print(d[-1])
#
# print(d[0][0])
# print(d[0,0])
# print(d[-1,-1])
# print(d[-1][-1])
#
# print(d[::-1])
#
# print(d[::-1][::-1])#마지막 행부터 읽고, 또 마지막 행부터 다시 읽어라.
# print(d[::-1,::-1])#마지막 행부터 읽고 마지막 열부터 읽어라
# print(d[1:3,2:4])
# print("-"*50)
# print(d)
# print(d.sum())
# print(d.sum(axis=1))#행단위로 합함.

# d2=np.arange(48).reshape(2,3,4,2)#2그룹? 3면 4행 2열 뒷쪽에서부터 분해=4차원, 주로 3차원 자주사용
# print(d2)
# print(d2.shape)


#길이가 1~10 인 정사각형 중, 길이가 짝수인 정사각형 넓이
areas=[]
#구문1
# for i in range(1,11):
#     if i%2==0:
#         areas.append(i*i)

#구문2
areas=[i*i for i in range(1,11) if i%2==0]
# for문을 돌면서 i를 하나씩 가져오고, if 조건에 맞는 i만 보낸다. 조건에 맞는 i를 원하는대로 계산해서 리스트에 넣는다.
print('areas: ',areas) #[4,16,36,100]

#(0,0)~(2,2)까지 출력
print([(x,y) for x in range(3) for y in range(3)])

students=['아톰','똘미','몽키','철이']
for number,name in enumerate(students):
    print('{}번의 이름은 {}입니다'.format(number+1,name))

#sut_dic={'1':'아톰','2':'똘이',...}만들기
# sut_dic={
#     '{}번'.format(number+1): for number,name in enumerate(students)
# }
# print(sut_dic)

students=['아톰','똘이','몽키','철이']
scores=[80,70,90,100]

# print(zip(students,scores))

stu_dic={
    # students: scores for students,scores in zip(students,scores)
    students[number]:scores[number] for number,name in enumerate(students)
}
print(stu_dic)

print("="*50)

a1 = [i for i in range(5)]
print(a1)

a2 = [0 for _ in range(5)]#변수값은 없지만 0으로 다섯번 반복해라
print(a2)

a3 = [[i,i*2+1,i*2-1] for i in range(5)]
print(a3)