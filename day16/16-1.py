import numpy as np
import pandas as pd
from pandas import DataFrame, Series
import matplotlib.pyplot as plt

# num=np.array(['3.14','-2.7','30'],dtype=np.string_)
# num=num.astype(float).astype(int)   #float 으로 변경하고 나서 정수로 변경 가능
# # num=num.astype(int)
#
# print(num)
#
# arr=np.arange(32).reshape((8,4)) ##>>>reshape에서 괄호한개와 두개의 차이 ==> 없음 그냥 써서 되면 되는거고 아님 마는거임
# print(arr)
# print(arr[[1,5,7,2],[0,3,1,2]]) #(1,0),(5,3),(7,1),(2,2) 각각의 좌표의 요소를 말함
#
# print(arr[[1,5,7,2]][:,[0,3,1,2]]) #[1,5,7,2]: 각 행, [0,3,1,2]:각 열에 대한 내가 원하는 순서를 지정

import random
# position=0
# walk=[]
# steps=1000
# for i in range(steps):
#     step = 1 if random.randint(0,1) else -1
#     position+=step
#     walk.append(position)
# print("position : ",position)
# print("walk : ", walk)
# print("minwalk : ",min(walk))
# print("maxwalk : ",max(walk))
# print(np.abs(walk))

obj=Series([1,2,-3,4])
print(obj)
print(obj.values) #값만 추출(속성, 함수)
print(obj.index)

obj = Series([1,2,-3,4],index=['x','y','z','k'])
print(obj)
print(obj['y'])
print(obj[['x','y','z']]) #인덱스 1개 참조시 [], 2개 이상 참조할 때는 대괄호 2개[[]]

print("="*30)
print(obj[obj>0])
print(obj*2)
print(np.exp(obj))

#null(초기회되지 않은 상태), na(결측치)
print(obj)
print('a' in obj)
print('x' in obj)

sdata = {'Ohio':35000,'Texas':71000,'Oregon':16000, 'Utah':5000} #딕셔너리를 활용하여 시리즈 추출//index :values
obj3=Series(sdata)
print(obj3)
print(type(obj3))
states=['California','Ohio','Oregon','Texas'] #리스트를 활용한 시리즈형식 추출
# obj99=Series(states)
# print(obj99)
obj4=Series(sdata,index=states) #딕셔너리(sdata)의 형식에 리스트(states)를 index로 사용
print(obj4)
print(pd.isnull(obj4))

#일반적인 개념 =>  nan : 숫자가 아닌 문자 같은 것 / na : 값이 누락 / nall : 값이 초기회 되지 않은 상태
#판다스 개념 => isnull함수 :na(null,nan) 인지 아닌지 확인 함수

print(obj3+obj4)

obj4.name='population'
obj.index.name='state'
print(obj4)

data={
    'state':['Ohio','Ohio','Ohio','Nevada','Nevada'],
    'year':[2000,2001,2002,2001,2002],
    'pop':[1.5,1.7,3.6,2.4,2.9]
}
frame=DataFrame(data)
print(frame)

print(DataFrame(data, columns=['year','state','pop'])) #출력 순서 변경

frame2=DataFrame(data, columns=['year','state','pop','debt'],index=['one','two','three','four','five'])
print(frame2)
print(frame2['state']) #특정 열 추출
print(frame2['year'])
print(frame2.ix['three']) #특정 행 추출
print('-'*40)
print(frame2[['state','year']])
print('-'*40)
print(frame2.ix[['three','five']])

print('-'*40)
print(frame2)
frame2['debt']=16.5
print(frame2)
frame2['debt']=np.arange(5) # arange의 값이 데이터의 길이가 같아야한다.
print(frame2)

print('-'*40)
val=Series([-1.2,-1.5,-1.7],index=['two','four','five']) #길이가 다른 데이터 열을 추가시 ->시리즈를 생성하여 추가한다.
print(frame2)
frame2['debt']=val
print(frame2)

print('-'*40)
frame2['eastern']=frame2.state=='Ohio'
print(frame2)

del frame2['eastern'] # 해당 열 지우기
print(frame2)

print(frame2.columns) #행의 목록 확인
print(frame2.index) #열의 목록 확인

print('-'*40)
pop={'Nevada':{2001:2.4,2004:2.9},'Ohio':{2000:1.5,2001:1.7,2002:3.6}}
frame3=DataFrame(pop)
print(frame3)
print('***')
print(frame3.T)

frame4=DataFrame(frame3, index=[2001,2002,2003])
print(frame4)

print('-'*40)
print(frame3)
pdata = {'Ohio':frame3['Ohio'][:-1],'Nevada':frame3['Nevada'][:2]} #데이터 길이가 안맞아도 series에서는 긴데이터에 맞춰서 출력
frame5=DataFrame(pdata)
print(frame5)