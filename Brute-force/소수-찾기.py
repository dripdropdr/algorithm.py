Programmers: https://school.programmers.co.kr/learn/courses/30/lessons/42839


# 소수를 찾을 때는, 어떤 수의 제곱근까지 검사함.
from itertools import permutations
def solution(numbers):
    n_list = []
    for i in range(1, len(numbers)+1):
        tmp = map(lambda x: int(''.join(x)), list(permutations(list(numbers), i)))
        n_list += [n for n in tmp if n not in[0, 1]]
    n_list = list(set(n_list))

    answer = 0
    for n in n_list:
        flg = True
        for i in range(2, int(n**(1/2)+1)):
            if n%i == 0: flg=False; break;
        if flg:  answer += 1
  
    return answer
