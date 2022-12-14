#  numbers	  return
# [6, 10, 2]	"6210"
# 0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.
# 예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 이중 가장 큰 수는 6210입니다.

def solution(numbers):
    str_numbers = list(map(lambda x: str(x), numbers))  
    str_numbers.sort(key=lambda x: x*3, reverse=True)
    answer = str(int("".join(str_numbers)))
        
    return answer

# 앞 자리에 큰 숫자를 이어 붙여야 그 결과가 가장 큰 숫자가 됨
# 3을 곱해서 sort하는 이유는 30, 3과 같은 케이스 때문 303 < 330
# str(int(string))를 통해서 000등의 경우 처리
