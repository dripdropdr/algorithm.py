https://school.programmers.co.kr/learn/courses/30/lessons/42885

def solution(people, limit):
    answer = 0
    people.sort()
    light_idx, heavy_idx = 0, len(people) - 1
    
    while light_idx <= heavy_idx:
        if people[light_idx] + people[heavy_idx] <= limit:
            light_idx += 1
        heavy_idx -= 1
        answer += 1
        
    return answer

# 비효율적인 이유: 어짜피 2명밖에 못 타는데 무게 여유가 생겨봤자 큰 의미가 없다... 너무 복잡하게 생각한듯 ?
def solution(people, limit):
    answer = 0
    
    
    while people:
        heavy = people[0]
        del people[0]
        
        most_acceptable = [0, 0] #weight, idx
        for peo_idx, peo in enumerate(people):
            if peo <= limit - heavy and most_acceptable[0] < peo:
                most_acceptable = [peo, peo_idx]
        
        if most_acceptable[0] != 0:
            del people[most_acceptable[1]]
            answer += 1
        else:
            answer += 1
        
    return answer
