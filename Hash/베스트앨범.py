Programmers: https://school.programmers.co.kr/learn/courses/30/lessons/42579#

'''
  1. 대응 정렬하는 코드는 무조건 알아가자!
  2. sorted(zip(list1, list2, list3, ...)) 하면 list1을 기준으로 정렬됨
  3. list.sort()는 객체 반환 x
  4. 애초에 plays로 정렬하여 song에 있는 리스트의 값을 바꾸는 케이스를 제외함

'''

from collections import defaultdict
def solution(genres, plays):
    answer = []
    total_play = defaultdict(int)
    song = defaultdict(list)

    for play, gen, idx in sorted(zip(plays, genres, range(len(plays))), reverse=True):
        total_play[gen] += play
        if len(song[gen]) < 2:
            song[gen].append(idx)
            if len(song[gen]) == 2 and plays[song[gen][0]] == play:
                song[gen].sort()
    
    sorted_dict = sorted(total_play.items(), key=lambda x: x[1], reverse=True)
    
    for gen, _ in sorted_dict:
        answer = answer + song[gen]
    
    return answer
