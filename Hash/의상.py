Programmers: https://school.programmers.co.kr/learn/courses/30/lessons/42578

'''
  1. 1은 key의 combination을 구한 후, 그때마다 각 kind의 개수를 구해주었으므로 for문을 반복적으로 쓸 수 밖에 없게됨
  2. 1에서는 해당 kind에서 아무것도 안 입는 경우를 고려하지 않았음. => 이 부분을 고려해야함
  3. 2에서는 각 Kind마다 안 입는 경우의 수를 고려하여 nC1+1, 그리고 모든 kind의 nC1+1을 곱해주고, 아무것도 안 입는 경우의 수 1을 제외하여 answer-1을 함.


'''

# 1) 1번 런타임 에러난 풀이 
from collections import defaultdict
from itertools import combinations
def solution(clothes):
    dict = defaultdict(list)
    for cloth, kind in clothes:
        dict[kind].append(cloth)
      
    answer = 0
    for i in range(1, len(dict)+1):
        for j in list(combinations(dict.keys(), i)): 
            tmp = 1
            for k in j:
                tmp *= len(dict[k])
            answer += tmp
    return answer


# 2) 최종 풀이
from collections import defaultdict
def solution(clothes):
    dict = defaultdict(list)
    for cloth, kind in clothes:
        dict[kind].append(cloth)
      
    answer = 1
    for kind in dict.keys():
        answer *= len(dict[kind])+1
      
    return answer-1
