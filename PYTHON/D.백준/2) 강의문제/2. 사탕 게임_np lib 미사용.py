'''
https://www.acmicpc.net/problem/3085
3
CCP
CCP
PPC

반례
https://www.acmicpc.net/board/view/58247
6
CCYYCC
YYCCYY
CCYYCC
YYCCYY
CCYYCC
YYCCYY

'''
n = int(input())  # 행
candy = [list(''.join(input())) for _ in range(n)]  # 배열
m = len(candy[0])  # 열
largest = 0


def count(list):
    count = 1
    max_count = 1
    for i in range(len(list) - 1):
        if list[i] == list[i + 1]:
            count += 1
            if count > max_count:
                max_count = count
        else:
            count = 1

    return max_count


for i in range(n):
    for j in range(m):
        for x, y in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            xx = i + x
            yy = j + y
            cnt = 0

            if 0 <= xx < m and 0 <= yy < n:
                tmp1, tmp2 = candy[i][j], candy[xx][yy]
                candy[i][j], candy[xx][yy] = candy[xx][yy], candy[i][j]

                a = count(candy[i])  # 현재 행
                b = count(candy[xx])  # 이전/다음 행
                c = count([c[j] for c in candy])  # 형재 열
                d = count([c[yy] for c in candy])  # 이전/다음 열

                if a > largest:
                    largest = a
                if b > largest:
                    largest = b
                if c > largest:
                    largest = c
                if d > largest:
                    largest = d

                candy[i][j], candy[xx][yy] = tmp1, tmp2

print(largest)
