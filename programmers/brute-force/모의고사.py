# answers	    return
# [1,2,3,4,5]	  [1]
# [1,3,2,4,2]	[1,2,3]
# 1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
# 2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
# 3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

# 1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 
# 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.


def solution(answers):
    answer = []
    score = [0,0,0]
    students = list(map(lambda x: x*(len(answers)), [[1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5]]))
    
    for idx, student in enumerate(students):
        for a, s in zip(answers, student):
            if a == s:
                score[idx] +=1

    for idx in range(3):
        if score[idx] == max(score):
            answer.append(idx+1)

    return answer
  
#   student1[answers_dx % len(student1)] 같은 모듈러 방식도 있음
