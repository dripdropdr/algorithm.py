Programmers: https://school.programmers.co.kr/learn/courses/30/lessons/12909

#   s	      answer
# "()()"	  true
# "(())()"	true
# ")()("	  false
# "(()("	  false

# 괄호가 바르게 짝지어졌다는 것은 '(' 문자로 열렸으면 반드시 짝지어서 ')' 문자로 닫혀야 한다는 뜻입니다.
# '(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때, 문자열 s가 올바른 괄호이면 true를 return 하고, 올바르지 않은 괄호이면 false를 return 하는 solution 함수를 완성해 주세요.
# 제한사항
# 문자열 s의 길이 : 100,000 이하의 자연수
# 문자열 s는 '(' 또는 ')' 로만 이루어져 있습니다.

# stack을 쓴 정직한 코드
def solution(bracket):
    answer = True
    sta = []
    for b in bracket:
        if b == '(' or not len(sta): sta.append(b)
        elif b == ')' and sta[-1] == '(': sta.pop()
        elif b == ')' and sta[-1] == ')': return False
    
    if len(sta): return False
    return True


# pair=0 을 기준으로 함
def is_pair(s):
    pair = 0
    for x in s:
        if pair < 0: break
        pair = pair + 1 if x == "(" else pair - 1 if x == ")" else pair
    return pair == 0
