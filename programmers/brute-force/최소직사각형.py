#               sizes	                            result
# [[60, 50], [30, 70], [60, 30], [80, 40]]	      4000
# [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]	  120
# [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]	  133
# 모든 명함의 가로 길이와 세로 길이를 나타내는 2차원 배열 sizes가 매개변수로 주어집니다. 
# 모든 명함을 수납할 수 있는 가장 작은 지갑을 만들 때, 지갑의 크기를 return 하도록 solution 함수를 완성해주세요.

def solution(sizes):
    maxw = 0
    maxh = 0
    for size in sizes:
        if size[0] > size[1]:
            w = size[0]
            h = size[1]
        else:
            w = size[1]
            h = size[0]
        if maxw < w:
            maxw = w
        if maxh < h:
            maxh = h
    answer = maxw * maxh
    return answer
