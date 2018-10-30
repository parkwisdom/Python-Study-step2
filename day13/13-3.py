import numpy as np

trees=np.loadtxt('../../Data/trees.csv',delimiter=',',skiprows=1,unpack=True)
#skiprows=1 : 첫줄을 건너뛰로 읽어 들여라. // unpack =Ture : 행과 열 변경, 3열 31행 -> 31열 3행 으로 변경됨
print(trees)
print(trees.shape)
print('='*50)
print(trees[:-1]) #"Girth","Height" 값들 출력
print('='*50)
print(trees[[-1]]) #"Volume" 값 출력