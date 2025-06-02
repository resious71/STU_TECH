# 
# 정렬 : 테이터를 특정 기준에 따라 순서대로 배열하는 것
#     -  컴퓨터 프로그래밍에서 매우 일반적
#     - 데이터 처리 및 검색에 매우 유용
# 
# 정렬 알고리즘
#     - 데이터를 어떻게 정렬할지를 결정하는 방법
#     
# Key Point
#    >> 얼마나 빨리 정렬을 수행할 수 있는가?
#    ==> 시간 복잡도와 장단점을 비교하여 알고리즘 사용
#  
# 거품 정렬(Bubble Sort)
#    - 근접한 데이터를 반복적으로 비교하여 작업 값을 앞으로 이동시키는 방식     
#    - 인접한 두 요소를 비교하면서 list의 한쪽 끝에서 다른 한쪽 긑으로 요소를 이동시키면서 
#      정렬하는 알고리즘
#    - 시간 복잡도가 O(n^2)으로 느리고 비효율적임 -> 대부분의 경우 다른 정렬 알고리즘을 사용 
# 
# # 거품 정렬(Bubble Sort):

import numpy as np

np.random.seed(31)
V = [*np.random.randint(1,100, 10)]
print(V)
for i in range(len(V)-1,0,-1):   # 자리
    for j in range(i):           # 비교
        if(V[j]>V[j+1]):
            V[j], V[j+1] = V[j+1], V[j]
print(V)
# 
# 선택 정렬
#    - 배열에서 가장 작은 값을 선택해 앞으로 이동시키면서 정렬하는 알고리즘 
#    - 정렬하려는 리스트에서 가장 작은 값을 찾아 맨 앞에 위치시키고 그 다음 작은 값을 찾아
#      다음 위치에 놓는 작업을 반복
#    - 시간 복잡도가 O(n^2)으로 거품 정렬과 동일함 
#    - 대규모 배열을 정렬할 때는 비효율적임

import numpy as np

np.random.seed(41)
V = [*np.random.randint(1,100, 10)]
print(V)
for i in range(len(V)-1):
    _min_i
    for j in range(i+1, len(V)):
        if V[j]<V[_min]:
            _min=j
    V[i], V[_min] = V[_min], V[i]
print(V)

