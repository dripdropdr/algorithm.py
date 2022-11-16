#dfs
def dfs(numbers, target, depth):
    global answer
    if depth == len(numbers):
        if sum(numbers) == target:
            answer += 1
            return 1
        else:
            answer += 0
            return 0
    else:
        dfs(numbers, target, depth + 1)
        numbers[depth] *= (-1)
        dfs(numbers, target, depth + 1)
        
def solution(numbers, target):
    global answer
    answer = 0
    dfs(numbers, target, 0)

    return answer
  
#bfs
def solution(numbers, target):
    answer = 0
    q = deque()
    q.append([numbers[0], 0])
    q.append([-1 * numbers[0], 0])

    while q:
        val, depth = q.popleft()
        # 종료조건
        if depth == len(numbers) - 1:
            if target == val:
                answer += 1
        else:
            q.append([(val + numbers[depth + 1]), depth + 1])
            q.append([(val - numbers[depth + 1]), depth + 1])

    return answer
 
