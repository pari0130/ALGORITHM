
# 05.완전탐색 기초

'''

'''
import sys
path = "D:/03.PERSNAL/00.STUDY/ALGORITHM/PYTHON/A.인프런/06.깊이넓이우선탑색(DFS,BFS) 활용/2) 휴가"
file = "/input.txt"
sys.stdin = open(path + file, "r")


def DFS(L, sum):
    global res
    if L == n + 1:
        if sum > res:
            res = sum
    else:
        if L + T[L] <= n + 1:  # 현재날짜의 수업을 진행
            DFS(L + T[L], sum + P[L])
        DFS(L+1, sum)  # 다음날자로 이동처리 (종료처리를 위해 n+1 날짜로 이동)


if __name__ == "__main__":
    n = int(input())
    T = list()
    P = list()
    for i in range(n):
        a, b = map(int, input().split())
        T.append(a)
        P.append(b)
    res = -2147000000
    T.insert(0, 0)
    P.insert(0, 0)
    DFS(1, 0)
    print(res)
