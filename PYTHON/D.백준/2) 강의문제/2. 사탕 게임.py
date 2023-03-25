'''
https://www.acmicpc.net/problem/3085
3
CCP
CCP
PPC

'''
import numpy as np

n = int(input())  # 행
candy = [list(''.join(input())) for _ in range(n)]  # 배열
m = len(candy[0])  # 열
largest = 0


def count(list):
    dict = {"C": 0, "P": 0, "Z": 0, "Y": 0}
    for i in range(len(list)):
        dict[list[i]] += 1
    return max([v for v in dict.values()])


for i in range(n):
    for j in range(m):
        for x, y in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            xx = i + x
            yy = y + y
            cnt = 0

            if 0 <= xx < m and 0 <= yy < n:
                tmp = candy[i][j]
                candy[i][j] = candy[xx][yy]
                candy_tmp = np.array(candy)

                a = count(candy_tmp[i, :])  # 현재 행
                b = count(candy_tmp[xx, :])  # 이전/다음 행
                c = count(candy_tmp[:, j])  # 형재 열
                d = count(candy_tmp[:, yy])  # 이전/다음 열

                if a > largest:
                    largest = a
                if b > largest:
                    largest = b
                if c > largest:
                    largest = c
                if d > largest:
                    largest = d

                candy[i][j] = tmp

print(largest)
