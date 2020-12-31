
# 05.완전탐색 기초

'''
1. 이항계수를 이용한 풀이를 해야함

'''
import sys
path = "D:/03.PERSNAL/00.STUDY/ALGORITHM/PYTHON/A.인프런/05.완전탐색 기초/10) 수열 추측하기(순열, 파스칼)"
file = "/input.txt"
sys.stdin = open(path + file, "r")


def DFS(L, sum):  # 레벨, 최종 값의 합
    if L == n and sum == f:
        for x in p:  # p는 순열 저장 위치
            print(x, end=' ')
        sys.exit(0)
    else:
        for i in range(1, n + 1):  # 1, 2, 3, 4
            if ch[i] == 0:
                ch[i] = 1
                p[L] = i
                DFS(L + 1, sum + (p[L] * b[L]))
                ch[i] = 0


if __name__ == "__main__":
    n, f = map(int, input().split())  # 4, 16
    p = [0] * n
    b = [1] * n  # list = [1, 1, 1, 1]
    ch = [0] * (n + 1)  # 순열 중복방지용
    for i in range(1, n):
        b[i] = b[i - 1] * (n - i) // i  # 1, 3, 3, 1 (이항 계산을 위해 곱해지는 값일 구하는 방법)
    DFS(0, 0)
    # for x in b:
    #     print(x)
