Programmers: https://school.programmers.co.kr/learn/courses/30/lessons/86491#qna

#               sizes	                            result
# [[60, 50], [30, 70], [60, 30], [80, 40]]	      4000
# [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]	  120
# [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]	  133
# 모든 명함의 가로 길이와 세로 길이를 나타내는 2차원 배열 sizes가 매개변수로 주어집니다. 
# 모든 명함을 수납할 수 있는 가장 작은 지갑을 만들 때, 지갑의 크기를 return 하도록 solution 함수를 완성해주세요.


# 대각선은 항상 자리를 많이 차지함 => 그려보고 판단
# 한 쪽으로 긴 면 몰아넣기
def solution(sizes):
    answer = 0
    long = []
    short = []
    for w, h in sizes:
        if w>h: long.append(w); short.append(h)
        else: long.append(h); short.append(w)
    
    return max(long) * max(short)
