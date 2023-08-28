Programmers: https://school.programmers.co.kr/learn/courses/30/lessons/42860#

def solution(name):
    if set(name) == {'A'}:
        return 0

    answer = float('inf')
    for i in range(len(name) // 2): # 모든 경우의 수 고려, but 반 이상 움직일 필요 없음
        left_moved = name[-i:]+name[:-i]
        right_moved = name[i::-1]+name[i+1:][::-1]
        # print(left_moved, right_moved)
        for n in [left_moved, right_moved]:
            # 해당 시나리오에서 안 갈 부분은 삭제함 -> 수평 이동량 계산하기 위해서
            while n and n[-1] == 'A':
                n = n[:-1]
            # 전체 이동량 계산 
            horizental = i + len(n)-1 # 
            vertical = 0
            for c in map(ord, n):
                vertical += min(c - 65, 91 - c)
            # 이동량 중 최소 선택
            answer = min(answer, horizental + vertical)

    return answer


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
