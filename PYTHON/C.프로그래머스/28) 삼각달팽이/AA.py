
'''
'''


from itertools import chain


def solution(n):
    # n층의 개수는 n개 -> 리스트화
    maps = [[0]*i for i in range(1, n+1)]
    # 인덱스 값은 0부터 시작하므로 y축에 -1, x축에 0
    y, x = -1, 0
    # 인덱스에 해당하는 값은 1부터
    number = 1
    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:
                y += 1
            elif i % 3 == 1:
                x += 1
            elif i % 3 == 2:
                y -= 1
                x -= 1
            maps[y][x] = number
            number += 1
    # chain을 활용하여 2차원 배열을 1차원으로 펴주기
    answer = [i for i in chain(*maps)]
    return answer


 # [1,2,9,3,10,8,4,5,6,7]
print("답 : ", solution(4))

# [1,2,12,3,13,11,4,14,15,10,5,6,7,8,9]
print("답 : ", solution(5))

# [1,2,15,3,16,14,4,17,21,13,5,18,19,20,12,6,7,8,9,10,11]
print("답 : ", solution(6))
