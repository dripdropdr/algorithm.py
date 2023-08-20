Programmers: https://school.programmers.co.kr/learn/courses/30/lessons/42860#

# Greedy - 하지만 이 문제는 그리디로 풀리지 않음 ㅋㅋ ㅋ ㅋㅋ 
def solution(name):
    answer = 0
    flg = [False if n != 'A' else True for n in name]
    i = 0
    for _ in range(len(name)):
        answer += min(ord(name[i]) - ord('A'), ord('Z') - ord(name[i])+1)
        flg[i] = True
        left_idx = [idx for idx, f in enumerate(flg) if not f]
        if left_idx:
            distance, idx = 21, 0
            for n in left_idx:
                if abs(i-n) < (i-0+len(name)-n): if abs(i-n) < distance: idx = n; distance = abs(i-n)
                else: if (i-0+len(name)-n) < distance: idx = n; distance = i-0+len(name)-n
            answer += distance
            i = idx
        else: break
          
    return answer
