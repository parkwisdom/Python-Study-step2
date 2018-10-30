#a=132
# if a%2==1:
#     print('홀수')
# else:
#     print('짝수')
#
# if a%2:
#     print('홀')
# else:
#     print('짝')
#
# a=0
# if a:
#     print('홀')
# else:
#     print('짝')
#
#     #입력 받은 정수가 음수/양수인지 0인지?
# b=int(input())
# #print(b+1)
# print(type(b))
#
# if b<0:
#     print('음수')
# else:
#     if b>0:
#         print('양수')
#     else:
#         print('제로')
#
# print('='*50)
#
# for i in range(10):
#     print(i, end=" ")
# print()
# for i in range(0,10):
#     print(i, end=" ")
# print()
# for i in range(0,10,1):
#     print(i, end=" ")
# print()
#
#
# for i in range(10-1, -1,-1):
#     print(i, end=" ")
# print()
# for i in reversed(range(10)):
#     print(i, end=" ")
# print()
#
# s=0
# for i in range(5):
#     s+=i
#     print(s)
# s=''
# for i in range(5):
#     s+=str(i+1)+" " #문자로 출력
#     print(s)
#
#
# #리스트
# a=[1,3,5]
# print(a[0],a[1],a[2])
# print(a)
# a[0]=a[2]
# print(a)
# a.append(11)
# print(a)
# #역순 출력
# for i in reversed(a):
#     print(i)
# print()
#
# for i in reversed(range(len(a))):
#     print(a[i])
# print()
#
# for i in range(len(a)-1,-1,-1):
#     print(a[i])
# print()
#
# a,b=3,8
# print(a,b)
# a,b = b,a
# print(a,b)
#
# #튜플:리스트의 상수 버전
# t=(1,3,5)
# print(t)
# print(t[0])
# # t[0]=9
# # print(t[1])
# print()
#
# t2=(100,200)
# print(t2)
# t2=100,200
# print(t2)
# t3,t4 =t2
# print(t2, type(t2))
# print(t3)
# print(t4)
## ---------------------------------

#
# def order(a,b):
#     if a<b:
#         return a,b
#     return b,a
# print(order(9,4))
#
# def order(a,b):
#     if a<b:
#         return a,b
#     return b,a
# min,max=order(9,4)
# print(max,min)
# _,max =order(9,4)
# print(max)
#
# #★★★★★중복값제거
# ns =[1,3,5,1,3,5,1,3,5]
# unique=[]
# for i in ns:
#     if not i in unique: #unique에 i값이 저장되어 있지 않다면
#         unique.append(i)
# print(unique)
#
# print(list(set(ns)))
#
#
# ns=[2,4,6,1,3,5]
# for i in range(len(ns)):
#     print(i, ns[i], end=', ')
# print()
#
# j=0
# for i in ns:
#     print(j,i)
#     j+=1
#
# for i in enumerate(ns): #0번째는 순서, 1번째는 요소가 입력되어 출력
#     print(i,"+",i[0],"+",i[1])
#
# for i,j in enumerate(ns):
#     print(i,j)
#
# def dummy():
#     #pass : 수행하지말고 지나가라
#     pass
# print(dummy())
#
# def cost_function(xx,yy,ww):
#     cost = 0
#     for i in range(len(x)):
#         hx=ww *x[i] #hx함수 = 10*x
#         #print(hx)
#         cost += (hx-y[i])**2 #기울기의 차를 구한다?
#     return cost/len(xx)
#
# x=[1,2,3]
# y=[1,2,3]
# #y=w*x
# w=3
# # print(cost_function(x,y,w))
# # print(cost_function(x,y,2))
# # print(cost_function(x,y,1))
#
# xxx,yyy=[],[]
# for i in range(-50,50):
#     w=i/10 #-5,-4.9 ,-4,8,...4.7, 4.8, 4.9
#     c = cost_function(x,y,w)
#     print(w,c)
#     xxx.append(w)
#     yyy.append(c)
# import matplotlib.pyplot as plt
# plt.plot(xxx,yyy)
# plt.plot(xxx,yyy,'ro')
# plt.show()
#
# a=dict(name='kim',age=20)
# print(a)
# print(a['name'])
# a['addr']='seoul'
# print(a)
#
# print(a.keys())
# print(a.values())
# print(a.items())
#
# for k in a.keys(): #속성값만 추출
#     print(k,a[k])
# print()
# for v in a.values():
#     print(v)
# print()
# for item in a.items():
#     print(item,item[0],item[1])
# print()
# for k,v in a.items():
#     print(k,v)
# print()
# for k in a:
#     print(k,a[k])
# print()
# for k in reversed(list(a.keys())):
#     print(k,a[k])

# a=[1,3,5,7,9]
# print(a[len(a)-1])
# print(a[0:len(a)//2])
# print(a[len(a)//2:len(a)])