Programmers: https://school.programmers.co.kr/learn/courses/30/lessons/42840

# answers	    return
# [1,2,3,4,5]	  [1]
# [1,3,2,4,2]	[1,2,3]
# 1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
# 2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
# 3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

# 1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 
# 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.


def solution(answers):
    result = [0,0,0]
    n1 = [1,2,3,4,5]
    n2 = [2,1,2,3,2,4,2,5]
    n3 = [3,3,1,1,2,2,4,4,5,5]
    for idx, ans in enumerate(answers):
        if n1[idx%5] == ans: result[0] += 1
        if n2[idx%8] == ans: result[1] += 1
        if n3[idx%10] == ans: result[2] += 1
    
    m = max(result)
    return [idx+1 for idx, n in enumerate(result) if n == m]
