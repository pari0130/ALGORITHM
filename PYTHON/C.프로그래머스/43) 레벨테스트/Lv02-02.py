'''
달팽이
'''
from itertools import chain


def solution(n):
    # n층의 개수는 n개 -> 리스트화
    maps = [[0] * i for i in range(1, n + 1)]
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
