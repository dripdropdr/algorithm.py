Programmers: https://school.programmers.co.kr/learn/courses/30/lessons/42746

#  numbers	  return
# [6, 10, 2]	"6210"
# 0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.
# 예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 이중 가장 큰 수는 6210입니다.

# 앞 자리에 큰 숫자를 이어 붙여야 그 결과가 가장 큰 숫자가 됨
# 3을 곱해서 sort하는 이유는 30, 3과 같은 케이스 때문 303 < 330
def solution(numbers):
    str_nums = list(map(lambda x: [(str(x)*4)[:4], str(x)], numbers))
    str_sorted = sorted(str_nums, reverse=True)
    
    res = ''.join(map(lambda x: x[1], str_sorted))
    if res.startswith('0'): return '0'
    return res


# sort에 붙일 수 있는 comparator 알아두기. functools.cmp_to_key()
import functools
def comparator(a,b):
    t1 = a+b
    t2 = b+a
    return (int(t1) > int(t2)) - (int(t1) < int(t2)) #  t1이 크다면 1  // t2가 크다면 -1  //  같으면 0

def solution(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key=functools.cmp_to_key(comparator),reverse=True)
    answer = str(int(''.join(n)))
    return answer
