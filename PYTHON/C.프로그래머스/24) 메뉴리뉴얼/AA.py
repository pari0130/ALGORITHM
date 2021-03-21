
'''
course의 숫자만큼 반복(2,3,5의 경우, 2개짜리 조합, 3개짜리 조합, 5개짜리 조합 찾기):
모든 order에 대해 반복:
order에 대해 course 값(2개,3개,5개...) 만큼 조합
(orderr: A,B,C,F,G / course: 2 )의 경우 AB, AC, AF, AG, BC, BF...
'XY'와 'YX' 등의 경우를 위해 미리 정렬해준뒤 조합(예제 3번의 경우)
조합된 주문(메뉴 'A' + 메뉴 'Z' :'AZ') 에 대해 모든 주문 내역에 있는 해당 조합(ex.'AZ')의 갯수를counter모듈을 이용하여 셈. 
해당 counter에 아무 값도 없거나(해당 주문 조합이 나온적이 없었거나), 최댓값이 1이면(해당 조합을 주문한 사람이 혼자라면) 패스
아니면 answer에 최댓값(현재 갯수에 해당하는 메뉴 조합 중 가장 많이 주문되었던 것) 을 가진 주문 조합을 다 넣는다.

'''

'''
포인트 : combinations(list, 구할조합의수) / Counter(temp)

'''




from collections import Counter
from itertools import combinations
def solution(orders, course):
    answer = []
    for c in course:
        temp = []
        for order in orders:
            # 조합의 개수 구하기, combinations(list, 구할조합의수)
            combi = combinations(sorted(order), c)
            temp += combi
        counter = Counter(temp)
        if len(counter) != 0 and max(counter.values()) != 1:
            answer += [''.join(f) for f in counter if counter[f]
                       == max(counter.values())]

    return sorted(answer)


print("답 : ", solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],
                       [2, 3, 4]))  # ["AC", "ACDE", "BCFG", "CDE"]

# print("답 : ", solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"],
#                        [2, 3, 5]))  # ["ACD", "AD", "ADE", "CD", "XYZ"]

# print("답 : ", solution(["XYZ", "XWY", "WXA"],
#                        [2, 3, 4]))  # ["WX", "XY"]
