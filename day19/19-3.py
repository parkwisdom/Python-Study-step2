#matplotlib

import matplotlib as mpl
import matplotlib.pylab as plt
import numpy as np

# plt.title('Plot')
# plt.plot([10,20,30,40],[1,4,9,16],'bD-.') #'rs--' : 빨간 점선 네모점, 'bo--' : 파란 점선 동그라미점, 'bD-.' : 파란 -.연속선 마름모점
# plt.xlim(0,50) #x축의 범위
# plt.ylim(-10,30) #y축의 범위


# x=np.linspace(-np.pi,np.pi,256) #-np.pi~np.pi까지 256개의 구간으로 나눔
# c=np.cos(x)
# plt.plot(x,c)
# plt.xticks([-np.pi,-np.pi/2,0 , np.pi/2, np.pi],['-pi','-pi/2','0','pi/2','pi'])
# plt.yticks([-1,0,1],['low','zero','higt'])


    # #여러 선 그리기
# t=np.arange(0.,5.,0.2)
# plt.plot(t,t,'r--', t,0.5*t**2,'bs:', t,0.2*t**3,'g^-')


    # #범례
# x= np.linspace(-np.pi, np.pi, 256)
# c,s =np.cos(x),np.sin(x)
# plt.plot(x,c,ls="--", label="cosine")
# plt.plot(x,s,ls=":", label="sine")
# # plt.legend() #디폴트(best):가장 적잘한 위치에 범례를 출력함
# plt.legend(loc=2) #loc==>1~10까지 설정가능 ==>디폴트값은 0
# plt.xlabel('xlabel')
# plt.ylabel('ylabel')
# plt.show()


#matplotlib : Figure, Axis ,Axes 객체로 구성
#Figure는 1개 이상의 Axes로 구성  =>1개의 figure에 그래프를 화면분할로 출력??!

# f1=plt.figure(figsize=(10,2)) #그림의 크기
# plt.plot(np.random.randn(100))

# f1=plt.figure(1)
# plt.plot([1,2,3,4],'ro:')
# f2=plt.gcf()
# print(f1,id(f1))
# print(f2,id(f2))
# plt.show()


    #화면나누기
x1=np.linspace(0.0,5.0)
x2=np.linspace(0.0,2.0)
y1=np.cos(2*np.pi*x1)*np.exp(-x1)
y2=np.cos(2*np.pi*x2)

ax1=plt.subplot(1,2,2)
plt.plot(x1,y1,'yo-')

ax2=plt.subplot(1,2,1)
plt.plot( x2,y2,'r.-')

plt.show()
# print(x1)
