Programmers: https://school.programmers.co.kr/learn/courses/30/lessons/84512?language=python3


from itertools import permutations
def solution(word):
    word_list = []
    for i in range(1,6):
        word_list += list(map(lambda x: ''.join(x), set(permutations(['A', 'E', 'I', 'O', 'U']*5, i))))
    return sorted(word_list).index(word)+1

# 이게 무슨 말인지 알고싶다 ... ...왜 등비수열의 합을 인덱스와 곱했는가
def solution(word):
    answer = 0
    for i, n in enumerate(word):
        answer += (5 ** (5 - i) - 1) / (5 - 1) * "AEIOU".index(n) + 1
    return answer
