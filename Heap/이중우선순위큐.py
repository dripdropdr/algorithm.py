Programmers: https://school.programmers.co.kr/learn/courses/30/lessons/42628

from collections import deque
def solution(operations):
    answer = deque([])
    for oper in operations:
        if oper == 'D 1':
            if len(answer): answer.pop()
        elif oper == 'D -1':
            if len(answer): answer.popleft()
        else:
            num = int(oper.replace('I ', ''))
            answer.append(num)
            answer = deque(sorted(answer))
        print(answer)
    
    if not len(answer): return [0, 0]
    else: return [answer.pop(), answer.popleft()]
