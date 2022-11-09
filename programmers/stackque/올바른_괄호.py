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


def solution(s):
    answer = True
    stack = []
    for i in s:
        if len(stack) == 0:
            if i == "(":  stack.append(i)
            else:
                answer = False
                return answer
        # stack isn't empty
        else:
            if i == "(":
                stack.append(i)
            else:
                if stack[-1] == "(":
                    stack.pop()
                else:
                    answer = False
                    return answer
    # string is end -> 이 부분을 더 깔끔하게 처리할 수 있을듯 ex) return len(stack) == 0
    if len(stack) == 0:
        answer = True
    else:
        answer = False
    
    return answer
