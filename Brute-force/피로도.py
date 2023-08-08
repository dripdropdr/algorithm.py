Programmers: https://school.programmers.co.kr/learn/courses/30/lessons/87946

from itertools import permutations
def solution(k, dungeons):
    answer = 0
    tmp = list(permutations(dungeons, len(dungeons)))
    for case in tmp: 
        k_cnt, cnt = k, 0
        for i, j in case:
            if k_cnt >= i: k_cnt -= j; cnt += 1;
        answer = max(answer, cnt)
      
    return answer
