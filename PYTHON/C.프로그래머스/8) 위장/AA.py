'''
프로그래머스 위장 문제
'''

import sys

# for 문 돌면 시간초과 걸리는듯..
# def solution(clothes):
#     answer = 0
#     for i in range(len(clothes)):
#         curWear = clothes[i]
#         answer += 1
#         for j in range(i, len(clothes)):
#             if curWear[1] != clothes[j][1]:
#                 answer += 1
#     print(answer)

#     return answer

clothes1 = [
    ["yellow_hat1", "headgear"],
    ["yellow_hat2", "headgear"],
    ["blue_sunglasses1", "eyewear"],
    ["blue_sunglasses2", "eyewear"],
    ["green_turban1", "headgear"],
    ["green_turban2", "headgear"],
    ["green_turban3", "headgear"]
]

clothes2 = [["crow_mask", "face"], [
    "blue_sunglasses", "face"], ["smoky_makeup", "face"]]


# 문제의 핵심은 의상별로 hash 짝을 담는게 아니라, 옷의 종류가 몇가지가 되는지 구해서
# 옷의 종류에 해당하는 총 경우의 수를 구해야 한다.
# 총 옷 조합의 수는 (각 종류 마다 옷의 갯수+1)를 다 곱한 후 -1을 하면 나옵니다. (-1 은 안입은 경우)

# 따라서 각 카테고리별로 다음과 같이 “해당 카테고리의 아이템을 장착하지 않는 경우” 한개를 더 추가해서 계산해야한다.
# (모자의갯수 + 1) * (바지의갯수 + 1) * (안경의갯수 + 1)
def solution(clothes):
    answer = {}
    for i in clothes:
        if i[1] in answer:
            answer[i[1]] += 1  # 포함되어 있는 경우 count 증가
        else:
            answer[i[1]] = 1  # 포함되어 있지 않은 경우 옷 1개 초기값 입력

    print(answer)
    cnt = 1

    for i in answer.values():
        cnt *= (i + 1)

    print(cnt-1)

    return cnt-1


solution(clothes1)
