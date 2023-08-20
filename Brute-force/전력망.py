Programmers: https://school.programmers.co.kr/learn/courses/30/lessons/86971#qna

def solution(n, wires):
    answer = []
    area = []
    # 제거하려는 전선을 하나씩 반복하며 시뮬레이션
    for i in range(len(wires)):
        rootNode = {}
        parent = [k for k in range(n+1)]
        for j in range(len(wires)):
            # 현재 제거하려는 전선은 parent union을 하지 않음
            if i == j:
                continue
            unionParent(parent, wires[j][0], wires[j][1])

      # 최종 parent가 무엇인지 확인 
        for i in range(1,len(parent)):
            if findParent(parent,parent[i]) in rootNode:
                rootNode[findParent(parent, parent[i])] += 1
            else:
                rootNode[findParent(parent, parent[i])] = 1
              
        area = list(rootNode.values())
        answer.append(abs(area[0] - area[1]))
    
    return min(answer)

# 재귀로 자기 자신이 parent인 전선까지 도달
def findParent(parent, wire):
    if parent[wire] != wire:
        return findParent(parent, parent[wire])
    return parent[wire]
# parent를 통합하여 parent 리스트에 기록
def unionParent(parent, wire1, wire2):
    wire1 = findParent(parent, wire1)
    wire2 = findParent(parent, wire2)

    if wire1 < wire2:
        parent[wire2] = wire1
    else:
        parent[wire1] = wire2
