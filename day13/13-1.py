# path = "example.txt"
# data=open(path).readline()
# print(data)

import json
path="example.txt"
records=[json.loads(line) for line in open(path,encoding='utf-8')]
# print(records[0])
# print(records[0]['tz'])

time_zones=[rec['tz'] for rec in records if 'tz' in rec]
# print(time_zones)
# print(time_zones[:20])

def get_counts(sequence):
    counts={} #counts라는 빈 딕셔너리 생성
    for x in sequence: #'America/New_York'이 읽어짐..
        if x in counts: #해당값이 이미 저장된 경우
            counts[x]+=1
        else: #해당값이 저장 안 된 경우
            counts[x]=1
    return counts
counts=get_counts(time_zones)
# print(type(counts))
# print(counts['America/New_York'])
# print(len(counts)) #도시의 개수(97개)
# print(len(time_zones)) #tz가 있는 행의 개수(3440개)

from  collections import defaultdict

def get_counts2(sequence):
    counts=defaultdict(int) #0으로 초기화해라, 위에 코딩의 if구문을 이용하여 저장 안 된 값을 저장하는 과정을 간소화함.
    for x in sequence:
        counts[x]+=1

    return counts

counts=get_counts2(time_zones)
# print(type(counts))
# print(counts['America/New_York'])
# print(counts)

def top_counts(count_dict, n=10):
    value_key_pairs=[(value,key) for key,value in count_dict.items()]
    # print(value_key_pairs[0])
    value_key_pairs.sort()
    # print(value_key_pairs[-n:])
# print(top_counts(counts,3)) #상위 10개 도시 출력

from collections import Counter #Counter 함수를 이용해서 위에 문장을 간소화(요소들의 개수 세고,상위 10개도시 출력)
counts=Counter(time_zones)
# print(counts.most_common(10))
# print(counts)

eng="sadklfdsalijsdfajkdd"
# print(Counter(eng))

#parndas :데이터분석 패키지(모듈(.py: 함수, 변수 등 구성 요소 묶음) 함수 또는 패키지의 묶음)

from  pandas import DataFrame, Series
import pandas as pd
frame=DataFrame(records) #데이터를 표형태로 변환
# print(frame)
# print(frame.info())
# print(frame['tz'][:10])

tz_counts=frame['tz'].value_counts()
# print(tz_counts[:10])

# 'tz' =''일 경우 & 'tz'키가 없는 경우
#na : Not Available(결측치)
clean_tz=frame['tz'].fillna('Missing') #'tz'키가 없는 경우 - 항목 자체가 없는 경우
# print(clean_tz)
clean_tz[clean_tz=='']='Unknown' #'tz' =''일 경우 - 항목은 있는데 값이 없는 경우
# print(clean_tz)

import matplotlib.pyplot as plt #시각화 함수
# tz_counts[:10].plot(kind='barh')
# plt.show()

# print(frame.a.dropna()) #na행 제거
# x="test1 test2 test3"
# print(x.split()) #분리

# x=frame.a.dropna()
results=Series([x.split()[0] for x in frame.a.dropna()])
# print(type(results))
# print(results.value_counts()[:5])

# print(frame.a.notnull()) #a라는 키가 있나?없나?
cframe = frame[frame.a.notnull()]
# print(cframe) #'a'키가 없는 행은 제거된 상태
# print(len(cframe))

# print(cframe.a) # == print(cframe['a'])

import numpy as np
# print(cframe.a.str.contains('Windows'))
os= np.where(cframe.a.str.contains('Windows'),'Windows','Not Windows')
# print(os[:5])
by_tz_os=cframe.groupby(['tz',os])  #cframe을 os별로 'tz'값에 따라 그룹화 해라
agg_counts = by_tz_os.size().unstack().fillna(0)#표를 재구성 할 때 쓰는 함수 : unstack
# print(agg_counts[:10])

indexer=agg_counts.sum(1).argsort()
# print(indexer[:10])

count_subset=agg_counts.take(indexer)[-10:]
print(count_subset)

#시각화
# normed_subset=count_subset.div(count_subset.sum(1), axis=0)
# normed_subset.plot(kind='barh',stacked=True)
count_subset.plot(kind='barh', stacked=True)
plt.show()
# s="My OS is Windows. "
# print(s.str.contanins('Linux'))