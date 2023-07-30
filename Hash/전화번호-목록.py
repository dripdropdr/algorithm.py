Programmers: https://school.programmers.co.kr/learn/courses/30/lessons/42577#

'''
주요점
1. 문자열로 된 숫자를 정렬했을 때 생기는 상황도 고려하자 
2. 접두사/접미사는 startswith/endswith
3. 원래는 phone_number 길이별로 잘라서 중복을 제거한 후 원래 phonebook과 길이를 비교하는 상황을 고려했는데, 이럴 경우 ["123", "1005", "1006", "1007"] 케이스에 위반된다. 

'''
# 시간복잡도: O(nlogn)
def solution(phone_book):
    phone_book = sorted(phone_book)
    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False
    return True

# Hash를 사용해서 푼 풀이
def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer
